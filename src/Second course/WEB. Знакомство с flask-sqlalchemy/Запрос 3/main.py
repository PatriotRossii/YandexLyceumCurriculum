database_path = input()

global_init(database_path)
db_session = create_session()

data = db_session.query(User).filter(
    User.age < 18
)

for user in data:
    print(f"<Colonist> {user.id} {user.surname} {user.name} {user.age} years")
