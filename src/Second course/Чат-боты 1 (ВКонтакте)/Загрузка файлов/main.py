import vk_api
import os


LOGIN, PASSWORD = "login", "password"
GROUP_ID = 204063703


def get_main_album_id(vk, group_id):
    albums = vk.photos.getAlbums(owner_id=f"-{group_id}")
    return min(
        albums["items"], key=lambda e: e["id"]
    )


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
    upload = vk_api.VkUpload(vk_session)

    main_album_id = get_main_album_id(vk, GROUP_ID)

    for filename in os.listdir("./static/img"):
        upload.photo(filename, main_album_id, GROUP_ID)


if __name__ == '__main__':
    main()
