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

    response = vk.friends.get(order="name", fields="bdate")
    for i, item in enumerate(response["items"]):
        ans = f"{i}) {item['last_name']} {item['first_name']}"
        if "bdate" in item:
            ans += f" {item['bdate']}"
        print(ans)


if __name__ == '__main__':
    main()
