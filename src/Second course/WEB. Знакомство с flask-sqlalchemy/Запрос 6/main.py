database_path = input()

global_init(database_path)
db_session = create_session()

data = db_session.query(Jobs).all()

max_collaborators = max(data, key=lambda e: len(e.collaborators.split(", ")))
max_count = len(max_collaborators.collaborators.split(", "))

result = filter(lambda e: len(e.collaborators.split(", ")) == max_count, data)

for job in result:
    leader = db_session.query(User).filter(User.id == job.team_leader)
    print(f"{leader.surname} {leader.name}")
