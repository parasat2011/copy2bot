

import telebot
import constants

bot = telebot.TeleBot(constants.token)

# bot.send_message(395762226, "test")

@bot.message_handler(content_types=['text'])
def handle_text(message) :
    if message.text == "Как дела?":
        bot.send_message(message.chat.id, "норм, ты как")
    elif message.text == "Че делаешь?":
        bot.send_message(message.chat.id, "да ничего особенного, учу бота разговаривать ))")
    elif message.text == "как успехи?":
        bot.send_message(message.chat.id, "пока что удовлетворительные, но стараюсь быстрее изучать")
    elif message.text == "привет":
        bot.send_message(message.chat.id, "привет")
    elif message.text == "хорошо":
        bot.send_message(message.chat.id, "))")
    elif message.text == "пойдет":
        bot.send_message(message.chat.id, "а должно быть хорошо")

    else:
        bot.send_message(message.chat.id, "Не верный запрос")



bot.polling(none_stop=True, interval=0)