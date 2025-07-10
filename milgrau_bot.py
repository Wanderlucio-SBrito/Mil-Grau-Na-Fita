import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Lista de ações monitoradas pelo usuário
acoes_monitoradas = []

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Olá! Eu sou o Mil Grau Na Fita!\nUse /adicionar PETR4 para monitorar uma ação.")

# Comando /adicionar
async def adicionar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        acao = context.args[0].upper()
        if acao not in acoes_monitoradas:
            acoes_monitoradas.append(acao)
            await update.message.reply_text(f"✅ Ação {acao} adicionada à lista.")
        else:
            await update.message.reply_text(f"⚠️ Ação {acao} já está sendo monitorada.")
    else:
        await update.message.reply_text("❌ Use: /adicionar <código_da_ação>")

# Comando /listar
async def listar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if acoes_monitoradas:
        texto = "📈 Ações monitoradas:\n" + "\n".join(f"- {a}" for a in acoes_monitoradas)
        await update.message.reply_text(texto)
    else:
        await update.message.reply_text("📭 Nenhuma ação sendo monitorada no momento.")

# Comando /topacoes
async def topacoes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Essa função será ativada em breve com dados das top ações da B3!")

# Inicialização do bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("adicionar", adicionar))
    app.add_handler(CommandHandler("listar", listar))
    app.add_handler(CommandHandler("topacoes", topacoes))
    print("✅ Bot iniciado. Aguardando mensagens...")
    app.run_polling()

if __name__ == "__main__":
    main()
