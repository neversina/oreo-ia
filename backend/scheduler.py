from datetime import datetime, time, timedelta
import zoneinfo

# Ajusta a timezone se necessário (ex.: "Europe/Lisbon")
TZ = zoneinfo.ZoneInfo("UTC")

REMINDERS = {
    "06:30": "Hora de acordar 🌅",
    "06:35": "Bebe água 💧",
    "06:40": "Higiene + aplicar pomada no rosto 🧴",
    "07:00": "Momento de oração 🙏",
    "07:30": "Hora de estudar programação 💻",
    "12:30": "Hora de almoçar 🍽️",
    "15:30": "Bebe água novamente 💧",
    "19:00": "Hora de jantar 🍽️",
    "21:00": "Tempo para dar atenção a quem te ama 🤍",
    "22:00": "Meditação / oração 🌙",
    "22:30": "Hora do banho 🚿",
    "23:00": "Hora de dormir 😴"
}

def _now_local():
    return datetime.now(TZ)

def daily_reminders(now: datetime | None = None) -> str | None:
    """
    Retorna a reminder correspondente à hora atual (se houver).
    Pode ser chamada periodicamente pelo frontend (ex.: a cada minuto).
    """
    if now is None:
        now = _now_local()
    hm = now.strftime("%H:%M")
    return REMINDERS.get(hm)

def next_reminder(now: datetime | None = None) -> tuple[str, datetime] | None:
    """
    Retorna o próximo lembrete e o datetime em que ocorrerá.
    """
    if now is None:
        now = _now_local()
    today = now.date()
    times = []
    for hhmm in REMINDERS.keys():
        hh, mm = map(int, hhmm.split(":"))
        dt = datetime.combine(today, time(hh, mm), tzinfo=TZ)
        if dt >= now:
            times.append(dt)
    if not times:
        # próximo é amanhã ao primeiro horario
        hh, mm = map(int, list(REMINDERS.keys())[0].split(":"))
        dt = datetime.combine(today + timedelta(days=1), time(hh, mm), tzinfo=TZ)
        return REMINDERS[list(REMINDERS.keys())[0]], dt
    next_dt = min(times)
    return REMINDERS[next_dt.strftime("%H:%M")], next_dt
