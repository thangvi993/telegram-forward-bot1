from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "7648064871:AAHl3wzBSxdPD295yTsjfag2Wt1KWbAS5fk"
SOURCE_CHAT_ID = -1002761454760  # Nhóm nguồn (Test1)
TARGET_CHAT_ID = -1002859256164  # Nhóm đích (Test2)

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == SOURCE_CHAT_ID:
        await context.bot.forward_message(
            chat_id=TARGET_CHAT_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, forward_message))
    app.run_polling()

if __name__ == "__main__":
    main()
