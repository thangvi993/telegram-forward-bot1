import os
import imghdr
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("TOKEN")
SOURCE_CHAT_ID = int(os.getenv("SOURCE_CHAT_ID"))
TARGET_CHAT_ID = int(os.getenv("TARGET_CHAT_ID"))

def forward_message(update, context):
    print(f"Received message in chat {update.message.chat_id}: {update.message.text}")
    if update.message.chat_id == SOURCE_CHAT_ID:
        print("Forwarding message...")
        context.bot.forward_message(
            chat_id=TARGET_CHAT_ID,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.all, forward_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
