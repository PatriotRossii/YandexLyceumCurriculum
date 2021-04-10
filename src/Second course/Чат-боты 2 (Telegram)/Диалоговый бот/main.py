from telegram.ext import CommandHandler, ConversationHandler, Updater, MessageHandler, Filters

TOKEN = ""


def start(update, context):
    update.message.reply_text(
        "Привет. Пройдите небольшой опрос, пожалуйста!\n"
        "Вы можете прервать опрос, послав команду /stop.\n"
        "Или пропустить данный вопрос, послав команду /skip.\n"
        "В каком городе вы живёте?")
    return 1


def first_response(update, context):
    message = update.message.text

    if message == "/skip":
        update.message.reply_text("Какая погода у вас за окном?")
    elif message == "/stop":
        return stop(update, context)
    else:
        update.message.reply_text(
            "Какая погода в городе {message}?".format(**locals()))

    return 2


def second_response(update, context):
    weather = update.message.text
    print(weather)
    update.message.reply_text("Спасибо за участие в опросе! Всего доброго!")
    return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Опрос прерван. Спасибо за участие.")
    return ConversationHandler.END


if __name__ == "__main__":
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('start', start)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(Filters.text, first_response)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(Filters.text, second_response)]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


