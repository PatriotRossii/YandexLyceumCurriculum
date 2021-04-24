import vk_api


LOGIN, PASSWORD = "login", "password"
GROUP_ID = 19291929
ALBUM_ID = 21382818


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

    response = vk.photos.get(owner_id=-GROUP_ID, album_id=ALBUM_ID)

    for i, item in enumerate(response["items"]):
        print(f"{i}) url: {item['url']}")
        print(f"width: {item['width']}; height: {item['height']}")


if __name__ == '__main__':
    main()
