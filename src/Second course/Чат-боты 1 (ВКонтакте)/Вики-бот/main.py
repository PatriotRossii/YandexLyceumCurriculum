import vk_api
import wikipedia
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

wikipedia.set_lang("ru")

TOKEN = "YOUR_TOKEN"
GROUP_ID = "YOUR_GROUP_ID"


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
                                 message="Доброго времени суток. Что хотите вы узнать?",
                                 random_id=random.randint(0, 2 ** 64))
                state[from_id] = 1
            else:
                try:
                    message = wikipedia.summary(event.obj.message['text'])
                    vk.messages.send(user_id=from_id,
                                     message=message,
                                     random_id=random.randint(0, 2**64))
                    vk.messages.send(user_id=from_id,
                                     message="Хотите узнать что-нибудь еще?",
                                     random_id=random.randint(0, 2**64))
                except wikipedia.DisambiguationError as e:
                    message = "Ошибка: " + e
                    vk.messages.send(user_id=from_id,
                                     message=message,
                                     random_id=random.randint(0, 2**64))


if __name__ == '__main__':
    main()
