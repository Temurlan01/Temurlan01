import telebot

TOKEN = "6580987501:AAFTVkCE7G59gXMjcnunBtC74-YhAWSs0fc"
bot = telebot.TeleBot(TOKEN)

YOUR_ID = 6197731316


questions = [
    "Какой ваш любимый цвет?",
    "Какая ваша любимая еда?",
    "Какое ваше любимое животное?"
]


user_answers = {}




def send_results_to_creator(creator_id):
    results = "\n".join(f"{user}: {answers}" for user, answers in user_answers.items())
    bot.send_message(chat_id=creator_id, text=f"Результаты опроса:\n\n{results}")

@bot.message_handler(commands=["start"])
def start(update, context):
    user_answers[update.effective_user.username] = []
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Давайте начнем опрос.\n\n")
    next_question(update, context, 0)


def next_question(update, context, question_index):
    if question_index < len(questions):
        current_question = questions[question_index]
        context.bot.send_message(chat_id=update.effective_chat.id, text=current_question)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Спасибо за участие!")
        send_results_to_creator(YOUR_ID)
        user_answers.clear()





bot.infinity_polling()
