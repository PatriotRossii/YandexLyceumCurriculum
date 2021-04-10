from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
import datetime

TOKEN = ""


def start(update, context):
    update.message.reply_text(
        "Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")
    update.message.reply_text(
        "Хотя нет. Вру. Могу подсказать вам текущую дату и время"
    )


def time(update, context):
    current_time = datetime.datetime.now().time()
    update.message.reply_text(
        f"Текущее время: {current_time.isoformat()}"
    )


def date(update, context):
    current_date = datetime.datetime.now().date()
    update.message.reply_text(
        f"Текущая дата: {current_date.isoformat()}"
    )


def echo(update, context):
    update.message.reply_text(update.message.text)


if __name__ == "__main__":
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("date", date))
    dp.add_handler(text_handler)

    updater.start_polling()
    updater.idle()
