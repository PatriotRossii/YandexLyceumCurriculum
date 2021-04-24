import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

TOKEN = "token"
GROUP_ID = "group_id"


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, GROUP_ID)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            from_id = event.obj.message["from_id"]

            resp = vk.users.get(user_ids=from_id, fields="city")
            user = resp[0]

            message = f"Привет, {user['first_name']}!" +\
                      (f" Как поживает {user['city']['title']}?" if "city" in user else "")

            vk.messages.send(user_id=from_id,
                             message=message,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
