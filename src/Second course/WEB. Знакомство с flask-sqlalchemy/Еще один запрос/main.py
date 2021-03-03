database_path = input()

global_init(database_path)
db_session = create_session()

department_1 = Department()
department_1.title = "Департамент геологической разведки"
department_1.chief = 1
department_1.members = "1, 2, 3"
department_1.email = "geo@mars.org"

department_2 = Department()
department_2.title = "Департамент продовольственного снабжения"
department_2.chief = 2
department_2.members = "1, 2, 3"
department_2.email = "supply@mars.org"

department_3 = Department()
department_3.title = "Департамент борьбы с классовыми врагами"
department_3.chief = 3
department_3.members = "1, 2, 3"
department_3.email = "guard@mars.org"

db_session.add(department_1)
db_session.add(department_2)
db_session.add(department_2)
db_session.commit()

department = db_session.query(Department).filter(
    Department.id == 1
).first()
department_members = [int(e) for e in department.members.split(", ")]

members = db_session.query(Users).filter(
    User.id.in_(department_members)
)
for member in members:
    jobs = db_session.query(Jobs).filter(
        Jobs.collaborators.ilike(f"%{member.id}%"), Jobs.is_finished == 1
    )
    total_count_of_hours = sum([e.work_size for e in jobs])

    if total_count_of_hours > 25:
        print(f"{member.surname} {member.name}")
