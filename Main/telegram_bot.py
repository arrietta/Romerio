import telebot
from telebot import types

from Romerio import settings

# Замените 'YOUR_BOT_TOKEN' на токен вашего Telegram бота
bot = telebot.TeleBot('6442182992:AAFF7xkljKsaHEmNh0PfE9k2rMXjZbGii0s')

def send_message_to_bot(message):
    try:
        chat_id = '@My_Alpha_Doors'
        bot.send_message(chat_id, message)
    except Exception as e:
        print(f"Произошла ошибка при отправке сообщения в Telegram: {str(e)}")

def send_photo_with_message_to_bot(link, message):
    try:
        print(f"{settings.BASE_DIR}{link}")
        chat_id = '@My_Alpha_Doors'
        photo_path = f"{settings.BASE_DIR}{link}"
        photo_input = types.InputFile(photo_path)
        bot.send_photo(chat_id, photo_input, caption=message)
    except Exception as e:
        print(f"Произошла ошибка при отправке сообщения в Telegram: {str(e)}")

if __name__ == "__main__":
    message = "This is a test message sent to the channel."
    send_message_to_bot(message)
