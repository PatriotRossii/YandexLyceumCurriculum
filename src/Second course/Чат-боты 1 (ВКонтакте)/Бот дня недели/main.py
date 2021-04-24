import vk_api
import wikipedia
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from datetime import datetime

wikipedia.set_lang("ru")

TOKEN = "YOUR_TOKEN"
GROUP_ID = "YOUR_GROUP_ID"

num_to_day = {
    0: "Понедельник", 1: "Вторник", 2: "Среда", 3: "Четверг", 4: "Пятница",
    5: "Суббота", 6: "Воскресенье"
}


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, GROUP_ID)

    state = {}

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            from_id = event.obj.message["from_id"]

            if state.get(from_id, None) is None:
                vk.messages.send(user_id=from_id,
                                 message="Доброго времени суток. Я могу сказать, в какой день недели"
                                         " была какая угодно дата. Введите только ее в формате YYYY-MM-DD",
                                 random_id=random.randint(0, 2 ** 64))
                state[from_id] = 1
            else:
                text = event.obj.message['text']
                try:
                    date = datetime.strptime(text, "%Y-%m-%d")
                except Exception as e:
                    print(e)
                    vk.messages.send(user_id=from_id,
                                     message="Ошибка. Некорректный формат данных",
                                     random_id=random.randint(0, 2 ** 64))
                    continue

                vk.messages.send(
                    user_id=from_id,
                    message=f"{text} было {num_to_day[date.weekday()]}. Введите еще дату, если изволите.",
                    random_id=random.randint(0, 2 ** 64)
                )


if __name__ == '__main__':
    main()
