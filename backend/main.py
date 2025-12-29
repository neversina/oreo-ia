from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from prompt import OREO_PROMPT
from scheduler import daily_reminders, next_reminder
import os
from dotenv import load_dotenv
import openai
import asyncio

load_dotenv()  # carrega .env se existir

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    # Não levantamos exceção automática aqui para facilitar desenvolvimento local,
    # mas os endpoints que chamam OpenAI falharão sem a chave.
    pass

openai.api_key = OPENAI_API_KEY

app = FastAPI(title="Oreo IA")

# Ajusta CORS conforme necessidade (frontend em outro domínio)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção, limitar ao domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserMessage(BaseModel):
    text: str

@app.get("/reminder")
async def reminder():
    """Retorna o reminder correspondente à hora atual (ou None)."""
    reminder = daily_reminders()
    return {"reminder": reminder}

@app.get("/next_reminder")
async def get_next_reminder():
    """Retorna o próximo reminder e timestamp."""
    nr = next_reminder()
    if nr is None:
        return {"next": None}
    reminder_text, dt = nr
    return {"next": {"text": reminder_text, "datetime": dt.isoformat()}}

@app.post("/chat")
async def chat(msg: UserMessage):
    """Encaminha a mensagem ao OpenAI usando o prompt da Oreo IA."""
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not configured on server")

    # Prepara payload para o ChatCompletion
    messages = [
        {"role": "system", "content": OREO_PROMPT},
        {"role": "user", "content": msg.text}
    ]

    # openai.ChatCompletion.create é bloqueante; executa em thread para não bloquear o loop
    def call_openai():
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

    try:
        response = await asyncio.to_thread(call_openai)
        reply = response.choices[0].message.content
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
