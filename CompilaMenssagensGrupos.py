

# openai.api_key = "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"
    # Substitua "SEU_BOT_TOKEN"     application = ApplicationBuilder().token("7826636428:AAHhFP-dZKdNm-Fky23NjqicNTo0-cHbsX4").build()

import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Configuração da API OpenAI
openai.api_key = "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"
 
# Função para iniciar o bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Olá! Eu sou o Message Summarizer Bot. Envie qualquer texto e eu vou resumi-lo para você!"
    )

# Função para resumir mensagens
async def summarize(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text

    try:
        # OpenAI API para resumo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente que resume textos."},
                {"role": "user", "content": f"Resuma este texto: {user_message}"}
            ]
        )
        summary = response['choices'][0]['message']['content'].strip()
        await update.message.reply_text(f"Resumo:\n{summary}")
    except Exception as e:
        await update.message.reply_text("Desculpe, algo deu errado. Tente novamente mais tarde.")
        print(f"Erro: {e}")

# Função principal para executar o bot
def main():
    application = ApplicationBuilder().token("7826636428:AAHhFP-dZKdNm-Fky23NjqicNTo0-cHbsX4").build()

    # Comando /start
    application.add_handler(CommandHandler("start", start))

    # Mensagens para resumir
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, summarize))

    print("Bot está rodando...")
    application.run_polling()

if __name__ == "__main__":
    main()
