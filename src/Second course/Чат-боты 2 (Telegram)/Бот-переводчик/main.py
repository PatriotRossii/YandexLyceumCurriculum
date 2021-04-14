from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler

# Command to install googletrans: pip install googletrans==3.1.0a0
import googletrans


TOKEN = "your_token"
START_KEYBOARD = ReplyKeyboardMarkup(
    [["ru-en", "en-ru"]], one_time_keyboard=False
)
AVAILABLE_LANGUAGES = ["ru", "en"]

translator = googletrans.Translator()


def echo(update, context):
    message = update.message.text
    languages = message.split("-")

    if len(languages) == 2 and [e in AVAILABLE_LANGUAGES for e in languages]:
        context.user_data["from"], context.user_data["to"] = languages
        update.message.reply_text(f"Выбрано направление перевода {message}")
    else:
        from_lang = context.user_data.get("from", None)
        to_lang = context.user_data.get("to", None)

        if from_lang and to_lang:
            update.message.reply_text(translator.translate(text=message, src=from_lang, dest=to_lang).text)


def start(update, context):
    update.message.reply_text(
        "Выберите направление перевода и пишите текст боту, чтобы он его перевел на выбранный вами язык."
        " Направление перевода по умолчанию: ru-en",
        reply_markup=START_KEYBOARD
    )
    context.user_data["from"], context.user_data["to"] = "ru", "en"


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, echo, pass_user_data=True))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
