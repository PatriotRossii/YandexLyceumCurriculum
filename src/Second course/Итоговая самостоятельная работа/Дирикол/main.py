import sqlite3

database_path = input()
specie = input()
country = input()


conn = sqlite3.connect(database_path)
cur = conn.cursor()

cur.execute("SELECT id FROM creatures WHERE type=?", [specie])
identifier = cur.fetchone()[0]

cur.execute("SELECT date FROM discovery WHERE creature_id=? "
            "ORDER BY DESC",
            [identifier])
for element in cur.fetchall():
    print(element[0])

conn.close()
