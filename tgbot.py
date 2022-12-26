import telebot

#создаем экземпляр бот
bot = telebot.Telebot("5785862157:AAE9KcMlHn7l6xmBSyEzEOD4hmWyERJZOtQ")

#функция, обрабатывающая команду / start
@bot.message_handler(commands=["start"]) #задаем команду с помощью handler(s)
def start(m, res=False): #m просто аргумент динамический
    bot.send_message(m.chat.id,'я на связию напиши мне что-нибудь')


    #запускаем сообщение от user
    bot.message_handler(content_types=["text"])
    def handle_text(message):
        bot.send_message(message.chat.id, 'вы написали: ' + message.text)

    #запускаем бот
    bot.polling(none_stop=True, interval=0)