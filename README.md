# 🚀 Automação de Início de Jornada de Trabalho

Este projeto é um script Python que automatiza sua rotina de trabalho logo ao ligar o computador. Ele realiza uma série de ações úteis para que você comece o dia com tudo pronto.

---

## 🧠 Objetivo

Evitar tarefas repetitivas do dia a dia e garantir que todas as ferramentas de trabalho estejam abertas e prontas assim que o sistema for iniciado.

---

## ⚙️ Funcionalidades

- 🔔 Exibe uma notificação de boas-vindas com lembrete da daily
- 🌐 Abre automaticamente os seguintes sites:
  - Gmail
  - Google Agenda
  - YouTrack
- 💬 Inicia o app do **Google Chat** (PWA via Chrome)
- Pode ser configurado para executar automaticamente ao iniciar o sistema

---

## 🛠️ Tecnologias utilizadas

- Python 3.x
- [`plyer`](https://pypi.org/project/plyer/) para exibir notificações nativas
- `webbrowser` e `os` (módulos padrão) para abrir sites e aplicativos

---


---

## 🔧 Configuração

### 1. Instale o Python (se ainda não tiver)

Certifique-se de que o Python esteja instalado e acessível no caminho, por exemplo:


### 2. Instale a biblioteca de notificação

Abra o terminal e execute:

```
pip install plyer
```

## ▶️ Execução automática ao ligar o computador

### 🔹 Passo 1: Criar um atalho

Crie um atalho com o seguinte comando (ajuste o caminho conforme necessário):
```
"C:\Python313\pythonw.exe" "C:\Scripts\abrir-sites.py"
```

> 📌 Obs: `pythonw.exe` executa o script em segundo plano, sem abrir a janela do terminal.

---

### 🔹 Passo 2: Adicionar à inicialização do Windows

1. Pressione `Win + R`
2. Digite: shell:startup e pressione Enter
3. A pasta **Inicializar** será aberta
4. Mova ou cole o atalho criado dentro dessa pasta

✅ Pronto! O script será executado automaticamente sempre que o computador for iniciado.



