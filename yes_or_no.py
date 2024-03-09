import telebot
import requests
import json

# тутна токен вашего бота
TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['yes_or_no'])
def send_yes_or_no(message):
    response = requests.get('https://yesno.wtf/api')
    data = json.loads(response.text)

    answer = data['answer']
    image_url = data['image']

    # Отправка гифки с подписью
    bot.send_animation(message.chat.id, image_url, caption=answer)


# Запуск обработчика сообщений
bot.infinity_polling()
