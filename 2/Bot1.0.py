import telebot

token =""
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Начнем наш опрос")


def send_simple_text(message):
    bot.reply_to(message, "Вы отправили обычное сообщение")
    message.text ="Привет"
bot.infinity_polling()

