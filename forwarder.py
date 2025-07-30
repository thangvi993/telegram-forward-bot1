import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Lấy token và chat_id từ biến môi trường
TOKEN = os.getenv("TOKEN")

SOURCE_CHAT_ID = os.getenv("SOURCE_CHAT_ID")
TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")

# Chuyển chat_id từ chuỗi sang int nếu có giá trị
SOURCE_CHAT_ID = int(SOURCE_CHAT_ID) if SOURCE_CHAT_ID else None
TARGET_CHAT_ID = int(TARGET_CHAT_ID) if TARGET_CHAT_ID else None

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
