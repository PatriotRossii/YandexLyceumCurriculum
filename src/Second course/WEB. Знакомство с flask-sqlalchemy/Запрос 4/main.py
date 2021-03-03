database_path = input()

global_init(database_path)
db_session = create_session()

data = db_session.query(User).filter(
    (User.position.ilike("%chief%") | User.position.ilike("%middle%"))
)

for user in data:
    print(f"<Colonist> {user.id} {user.surname} {user.name} {user.position}")
