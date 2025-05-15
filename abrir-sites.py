import webbrowser
import os
import time
from plyer import notification

time.sleep(5)

try:
    notification.notify(
        title="Bom dia, Tiago!",
        message="Lembrete: Daily às 11h15 com o time de Mobile. 🚀",
        timeout=10
    )
except Exception as e:
    print("Erro ao exibir notificação:", e)

# Abrir os sites principais
webbrowser.open("https://mail.google.com/mail/u/0/?ogbl#inbox")
webbrowser.open("https://calendar.google.com/calendar/u/0/r")
webbrowser.open("https://nectar.myjetbrains.com/youtrack/dashboard?id=539-104")

# Abrir o app PWA do Google Chat
os.startfile("C:\\Users\\nectar\\Desktop\\Google Chat.lnk")
