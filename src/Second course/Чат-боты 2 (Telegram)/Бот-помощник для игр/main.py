import random

from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup

TOKEN = ""


dices = {
    "кинуть один шестигранный кубик": lambda: [random.randint(1, 6)],
    "кинуть 2 шестигранных кубика одновременно": lambda: [random.randint(1, 6) for _ in range(2)],
    "кинуть 20-гранный кубик": lambda: [random.randint(1, 20)],
}

timers = {
    "30 секунд": lambda: 30,
    "1 минута": lambda: 60,
    "5 минут": lambda: 300,
}

exit_var = [["вернуться назад"]]


start_markup = ReplyKeyboardMarkup(
    [["/dice", "/timer"]], one_time_keyboard=True
)
dice_markup = ReplyKeyboardMarkup(
    [[e] for e in dices.keys()] + exit_var, one_time_keyboard=False
)
timer_markup = ReplyKeyboardMarkup(
    [[e] for e in timers.keys()] + exit_var, one_time_keyboard=True
)
close_markup = ReplyKeyboardMarkup(
    [["/close"]], one_time_keyboard=True
)


def start(update, context):
    update.message.reply_text(
        "Клавиатура подана",
        reply_markup=start_markup
    )


def dice(update, context):
    update.message.reply_text(
        "Клавиатура подана",
        reply_markup=dice_markup
    )


def timer(update, context):
    update.message.reply_text(
        "Клавиатура подана",
        reply_markup=timer_markup
    )


def message(update, context):
    msg = update.message.text
    if msg == "вернуться назад":
        start(update, context)

    elif msg in dices.keys():
        update.message.reply_text(" ".join([str(e) for e in dices[msg]()]))
    elif msg in timers.keys():
        due = timers[msg]()

        update.message.reply_text(f"засек {msg}")
        set_timer(context, update.message.chat_id, due, msg)

        update.message.reply_text(
            "Если желаете сбросить таймер - сделайте это!",
            reply_markup=close_markup
        )


def remove_job_if_exists(name, context):
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def set_timer(context, chat_id, due, msg):
    remove_job_if_exists(
        str(chat_id),
        context
    )
    context.job_queue.run_once(
        task,
        due,
        context=(chat_id, msg),
        name=str(chat_id)
    )


def task(context):
    job = context.job
    context.bot.send_message(job.context[0], text=f"{job.context[1]} истекло",
                             reply_markup=timer_markup)


def unset_timer(update, context):
    chat_id = update.message.chat_id
    remove_job_if_exists(str(chat_id), context)
    context.bot.send_message(chat_id, text=f"Таймер отменен",
                             reply_markup=timer_markup)


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("dice", dice))
    dp.add_handler(CommandHandler("timer", timer))
    dp.add_handler(CommandHandler("close", unset_timer))

    text_handler = MessageHandler(Filters.text, message)
    dp.add_handler(text_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
