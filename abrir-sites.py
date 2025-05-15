import webbrowser
import os
import time
from plyer import notification

time.sleep(5)

try:
    notification.notify(
        title="Bom dia, (seu nome)!",
        message="Lembrete: Daily às (horario) com o time de (time da Daily). 🚀",
        timeout=10
    )
except Exception as e:
    print("Erro ao exibir notificação:", e)

# Abrir os sites principais
webbrowser.open("https://mail.google.com/mail/u/0/?ogbl#inbox")
webbrowser.open("https://calendar.google.com/calendar/u/0/r")
webbrowser.open("https://(url do youtrack ou outra plataforma)")

# Abrir o app PWA do Google Chat
os.startfile("C:\\Desktop\\Google Chat.lnk")
