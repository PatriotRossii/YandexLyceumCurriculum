database_path = input()

global_init(database_path)
db_session = create_session()

data = db_session.query(User).filter(
    User.address == "module_1", User.speciality.notilike("%engineer%"), User.position.notilike("%engineer%")
)

for user in data:
    print(user.id)
