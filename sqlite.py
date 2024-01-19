import sqlite3

file = sqlite3.connect("base_people.file")
sql = file.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS USERS(
  login TEXT,
  password TEXT,
  cash BIGINT
)""")

file.commit()

user_login = input("login: ")
user_password = input("password: ")

sql.execute("SELECT login FROM users")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES(?, ?, ?)", (user_login, user_password, 0))
    file.commit()
    print("Зарегистрировано")
else:
    print("Такая информация уже имеется!")

    for value in file.execute("SELECT * FROM users"):
        print(value)