from typing import Text
import telebot

bot = telebot.TeleBot('5058346875:AAFCcTGUCnZ0BKUjpwxq1keCeokgX4JF-uE')

joined_file = open("joined.txt", 'w') #если файл не создан, создаем его
joined_file.close()

joined_file = open("joined.txt")
joined_users = set() #set работает лучше массива, т.к в set нельзя добавить 2 одинаковых id
for i in joined_file:
    joined_users.add(i.strip())
joined_file.close()

@bot.message_handler(commands=['start']) #добавляем id участника бота в файл
def start(message):
    if not str(message.chat.id) in joined_users:
        joined_file = open("joined.txt", "a")
        joined_file.write(str(message.chat.id)+'\n')
        joined_users.add(message.chat.id)

@bot.message_handler(commands=['announce'])
def announce(message):
    announcement = message.text[message.text.find(' ')+1::]
    if "gimnazpass271" in announcement:
        text = announcement[(announcement.find("-text")+6):announcement.find(" -img")]
        image_url = announcement[announcement.find("-img")+5::]
        for user in joined_users:
            bot.send_message(user, text)
            bot.send_photo(chat_id=joined_users, photo=image_url)
bot.polling()
