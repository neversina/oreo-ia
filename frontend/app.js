async function send() {
  const text = document.getElementById("msg").value;
  if (!text) return;
  document.getElementById("reply").innerText = "A Oreo IA está a pensar...";

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({text})
    });
    const data = await res.json();
    document.getElementById("reply").innerText = data.reply ?? "Sem resposta.";
  } catch (err) {
    document.getElementById("reply").innerText = "Erro ao contactar o servidor.";
  }
}

async function checkReminder() {
  try {
    const res = await fetch("/reminder");
    const data = await res.json();
    if (data.reminder) {
      document.getElementById("reminder").innerText = data.reminder;
    } else {
      document.getElementById("reminder").innerText = "";
    }
  } catch (err) {
    // silêncio
  }
}

document.getElementById("send").addEventListener("click", send);
setInterval(checkReminder, 60_000);
checkReminder();
