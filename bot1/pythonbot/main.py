import json
import random
import re
import telebot
from random import choice
from telebot import types
TOKEN = '1189478215:AAFTUt8WpYy-U8fmJcIyw_n2VgqnIvNwRBs'

#print(data)
#print(len(data), type(data))

#print(data)
'''
text=input()
a=text.split()#ввод пользователя

for i in range(len(data)):#пробегаем по всем анекдотам и сравниваем их
    b=data[i]['text_main'].split()
    max_count=len(b)

    jb=0
    print(b)
    print(a)
    for j in range(len(a)):#сравнение анекдота происходит через сравнение слов в нём
        if jb==len(b):
            break
        elif a[j]==b[jb]:
            count+=1
        jb+=1
    print(count, "/", max_count)
    if count==max_count:#если нашли анекдот точ в точь, как нам преслал пользователь, то выходим
        max_count_of_all=max_count
        index_of_anecd=i
        break
    else:
        if count/max_count>=max_count_of_all:
            max_count_of_all=count/max_count
            index_of_anecd=i
        count=0
new_anec=[]
if max_count_of_all>=0.5:
    print("Уууу, дружок, ты прислал мне баян")
    all_score+=1
else:
    print("Ух ты, это что-то новенькое")
    new_anec.append(text)
    all_score+=2
'''



#   fun = ["Рост", "Олег", "Ростислав", "Илья", "Инденбом", "Ад", "Фронтенд", "", ""]
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('C:\\Users\\ansko\\Desktop\\bot1\\welcome.jpeg', 'rb')
    mk2 = types.ReplyKeyboardRemove()
    bot.send_photo(message.chat.id, sti, reply_markup = mk2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("next")
    markup.add(item1)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, созданный, чтобы оценивать твои анекдоты.".format(message.from_user, bot.get_me()),
        parse_mode = 'html', reply_markup=markup)

    markup1=types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Так, теперь поехали. \n Ты вводишь свой анекдот, а мы ему выставляем оценку по шкале от 1 до 10, также мы проверяем баян твой анекдот или нет.", reply_markup = markup1)
    bot.register_next_step_handler(message, main_shit)
@bot.message_handler(content_types=['text'])
def main_shit(message):
    with open('all_anekdotes.json', 'r') as file:
        json_text=file.read()
        data=json.loads(json_text)

        entry_text = message.text  # ввод пользователя
        entry_text = "".join(re.findall("[а-яА-Я0-9 ]+", entry_text)).lower()
        if entry_text.isdigit() or entry_text.isspace() or len(entry_text) < 60:
            bot.send_message(message.chat.id, "Не рофли со мной, введи по нормальному")
        else:
            names = ["николай", "рост", "ростислав", "саша", "олег", "дима", "творог", "илья", "гоша", "андрей",
                     "денис", "гоша", "фёдор", "федор", "фёдр", "федр"]
            all_score = 0
            a = entry_text.lower().split()
            count = 0
            flag = 0
            max_count = 0
            index_of_anecd = 0
            max_count_of_all = 0
            for i in range(len(data)):  # пробегаем по всем анекдотам и сравниваем их
                b = data[i]['text_main'].split()
                max_count = len(b)
                jb = 0
                for j in range(len(a)):  # сравнение анекдота происходит через сравнение слов в нём
                    if jb == len(b):
                        break
                    if a[j] in names and flag == 0:
                        flag = 1
                    elif a[j] == b[jb]:
                        count += 1
                    jb += 1
                # print(count, "/", max_count)
                if count == max_count:  # если нашли анекдот точ в точь, как нам преслал пользователь, то выходим
                    max_count_of_all = max_count
                    index_of_anecd = i
                    break
                else:
                    if count / max_count >= max_count_of_all:
                        max_count_of_all = count / max_count
                        index_of_anecd = i
                    count = 0

            new_anec = []

            negative_result = ["Попахивает баяном", "Где-то я уже это видел", "Где-то я уже это слышел",
                               "Ух ты, ты прислал мне баян"]
            positive_result = ["Ух ты, это что-то новенькое", "Наверное, я отправлю это Росту", "Этого я ещё не видел",
                               "Поздравляю, "]
            if max_count_of_all >= 0.5:
                if flag == 1:
                    all_score += 1
                bot.send_message(message.chat.id, choice(negative_result))
                if int(data[index_of_anecd]['likes']) >= 2000:
                    all_score += 1
                elif int(data[index_of_anecd]['likes']) >= 3000:
                    all_score += 2
                elif int(data[index_of_anecd]['likes']) >= 4000:
                    all_score += 3
            else:
                if flag == 1:
                    all_score += 1
                if int(data[index_of_anecd]['likes']) >= 4000:
                    all_score += 3
                elif int(data[index_of_anecd]['likes']) >= 3000:
                    all_score += 2
                elif int(data[index_of_anecd]['likes']) >= 2000:
                    all_score += 1
                bot.send_message(message.chat.id, choice(positive_result))
                new_anec.append(entry_text)
                all_score += 2
            bot.send_message(message.chat.id, f"Оценка твоего анекдота :{all_score} / 5 баллов")


bot.polling(none_stop=True)
'''
    entry_text1 = message.text
    entry_text = entry_text1.split(" ")
    #bot.send_message(message.chat.id, entry_text)

#bot.polling(none_stop=True)

    count = 0
    max_count = 0
    index_of_anecd = 0
    max_count_of_all = 0
    for i in range(len(data)):  # пробегаем по всем анекдотам и сравниваем их
        b = data[i]['text_main'].split()
        max_count = len(b)
        jb = 0

        for j in range(len(entry_text)):  # сравнение анекдота происходит через сравнение слов в нём
            if jb == len(b):
                break
            elif entry_text[j] == b[jb]:
                count += 1
            jb += 1

        if count == max_count:  # если нашли анекдот точ в точь, как нам преслал пользователь, то выходим
            max_count_of_all = max_count
            index_of_anecd = i
            bot.send_message(message.chat.id, index_of_anecd)
            bot.send_message(message.chat.id, max_count_of_all)
                break
        else:
            if count / max_count >= max_count_of_all:
                max_count_of_all = count / max_count
                index_of_anecd = i
                bot.send_message(message.chat.id, index_of_anecd)
                bot.send_message(message.chat.id, max_count_of_all)
            count = 0
        new_anec = []
        all_score = 0
        if max_count_of_all >= 0.5:
            bot.send_message(message.chat.id, f"Уууу, дружок, ты прислал мне баян, и у тебя {all_score} очков")
            all_score += 1
        else:
            bot.send_message(message.chat.id, f"Ух ты, это что-то новенькое, это редкость. У тебя {all_score} очков")
            new_anec.append(entry_text1)
            all_score += 2
            



bot.polling(none_stop=True)
'''
