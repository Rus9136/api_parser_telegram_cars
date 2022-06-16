import telebot
import config


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['exchange'])
def exchange_comand(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('USD', callback_data='get-USD'),
                 telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'),
                 telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR')
                 )
    bot.send_message(
        message.chat.id,
        'Click on the currency of choice:',
        reply_markup=keyboard
    )






@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")





bot.polling(none_stop=True, interval=0)