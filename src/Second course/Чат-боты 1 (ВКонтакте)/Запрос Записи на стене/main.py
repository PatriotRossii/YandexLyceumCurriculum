import vk_api
import datetime

LOGIN, PASSWORD = "login", "password"


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция. """

    # Код двухфакторной аутентификации,
    # который присылается по смс или уведомлением в мобильное приложение
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(
        login, password,
        # функция для обработки двухфакторной аутентификации
        auth_handler=auth_handler
    )

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()

    response = vk.wall.get(count=5)
    for item in response["items"]:
        time_object = datetime.datetime.fromtimestamp(int(item["date"]))

        date = time_object.date().isoformat()
        time = time_object.time().isoformat(timespec="auto")

        print(f"{item['text']};")
        print(f"date: {date}, time: {time}")


if __name__ == '__main__':
    main()
