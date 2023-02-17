import telebot
from mod_calc import *

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, "Добро пожаловать в калькулятор!\nВведите первое число")
    bot.register_next_step_handler(message, get_num_1)


def get_num_1(message):
    global num_1
    num_1 = message.text
    if num_1.isdigit():
        bot.send_message(message.chat.id, f"Введите второе число")
        bot.register_next_step_handler(message, get_num_2)
    else:
        bot.send_message(
            message.chat.id, "Это не число, введите первое ЧИСЛО")
        bot.register_next_step_handler(message, get_num_1)


def get_num_2(message):
    global num_2
    num_2 = message.text
    if num_2.isdigit():
        bot.send_message(
            message.chat.id, f"Введите действие: + - * /")
        bot.register_next_step_handler(message, сalculations)
    else:
        bot.send_message(
            message.chat.id, "Это не число, введите второе ЧИСЛО")
        bot.register_next_step_handler(message, get_num_2)


def сalculations(message):
    global result
    if message.text == '+':
        result = sum_nums(num_1, num_2)
        bot.send_message(message.chat.id, f'{num_1} + {num_2} = {result}')
    elif message.text == '-':
        result = subtraction_nums(num_1, num_2)
        bot.send_message(message.chat.id, f'{num_1} - {num_2} = {result}')
    elif message.text == '*':
        result = multiplication_nums(num_1, num_2)
        bot.send_message(message.chat.id, f'{num_1} * {num_2} = {result}')
    elif message.text == '/':
        try:
            result = division_nums(num_1, num_2)
            bot.send_message(message.chat.id, f'{num_1} / {num_2} = {result}')
        except ZeroDivisionError:
            bot.send_message(message.chat.id, f'Делить на 0 НЕЛЬЗЯ')      
    else:
        bot.send_message(
            message.chat.id, "Данное действие не входит в функционал данного калькулятора, выберите действие: + - * /")
        bot.register_next_step_handler(message, сalculations)
    bot.send_message(
        message.chat.id, "Работа калькулятора завершена, для продолжения работы нажмите/введите => /start")


bot.polling(none_stop=True)
