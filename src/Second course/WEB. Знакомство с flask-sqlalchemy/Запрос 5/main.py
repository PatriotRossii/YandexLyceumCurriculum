database_path = input()

global_init(database_path)
db_session = create_session()

data = db_session.query(Jobs).filter(
    Jobs.work_size < 20, Jobs.is_finished == 0
)

for job in data:
    print(f"<Job> {job.job}")
