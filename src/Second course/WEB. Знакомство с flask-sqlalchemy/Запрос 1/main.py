database_path = input()

global_init(database_path)
db_session = create_session()

for user in db_session.query(User).filter(User.address == "module_1"):
    print(user)