import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

from datetime import tzinfo, timedelta
from datetime import datetime


TOKEN = "token"
GROUP_ID = "group_id"


class MoscowTZ(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=3)

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "+03:00"

    def __repr__(self):
        return f"{self.__class__.__name__()}"


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, GROUP_ID)

    TRIGGER_WORDS = [
        "время", "число", "дата", "день"
    ]
    tz = MoscowTZ()

    STANDARD_ANSWER = "Вы можете узнать сегодняшнюю дату, московское время и день недели, " \
                      "отправив нашему прекрасному боту сообщение, содержащее одно из следующих " \
                      "слов: время, число, дата, день"

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            from_id = event.obj.message["from_id"]

            reply = False
            words = event.obj.message["text"].split()
            for word in words:
                if word in TRIGGER_WORDS:
                    reply = True
                    break

            if reply:
                time_obj = datetime.now(tz=tz)

                date = time_obj.date()

                answer = f"Дата: {date.isoformat()}\n" +\
                    f"Время: {time_obj.time().isoformat()}\n" +\
                    f"День недели: {date.strftime('%A')}"
            else:
                answer = STANDARD_ANSWER

            vk.messages.send(user_id=from_id,
                             message=answer,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
