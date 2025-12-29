# 🖤 Oreo IA 🤍

Assistente pessoal inteligente para programadores.
Ajuda com código, rotina diária, hábitos, fé e equilíbrio.

Estrutura do projecto:
oreo-ia/
│
├── backend/
│   ├── main.py
│   ├── prompt.py
│   ├── scheduler.py
│   ├── database.py
│   └── requirements.txt
│
├── Dockerfile
├── README.md
└── .env.example

Como correr localmente:
1. Clona o repositório:
   git clone https://github.com/neversina/oreo-ia
2. Cria um virtualenv e instala dependências:
   cd oreo-ia/backend
   python -m venv .venv
   source .venv/bin/activate     # ou .venv\\Scripts\\activate no Windows
   pip install -r requirements.txt
3. Configura as variáveis:
   - Copia `.env.example` para `.env` e define `OPENAI_API_KEY`
4. Corre a API:
   uvicorn backend.main:app --reload --port 8000
5. Serve o frontend (ex.: abrir frontend/index.html no browser) ou usar um simples servidor estático:
   npx http-server frontend -c-1

Notas de segurança:
- Nunca commites chaves API. Usa .env e configura segredos no serviço de deploy.
- Em produção, limita `CORS` ao domínio do frontend.

Próximos passos sugeridos:
- Transformar o frontend numa PWA
- Containerizar com Docker + Docker Compose
- Adicionar testes e CI/CD
- Integrar persistência de utilizadores e lembretes com Supabase ou outra BD

Feito com carinho ❤️🖤
