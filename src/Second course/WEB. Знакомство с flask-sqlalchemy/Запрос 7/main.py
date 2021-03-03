database_path = input()

global_init(database_path)
db_session = create_session()

data = db_session.query(User).filter(
    User.age < 21, User.address == "moudle_1"
)

for user in data:
    user.address = "module_3"
db_session.commit()
