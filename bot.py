import telebot

bot = telebot.TeleBot("7012461173:AAFQ5WMc6YCd9sSxLOSyO98tpoZQ-4kyi0Q")

@bot.message_handler(commands=["start"])
def start_command(message):
  bot.send_message(message.chat.id, "Hi baby,em bé của tôi dạo này ổn chứ?")

bot.polling()
