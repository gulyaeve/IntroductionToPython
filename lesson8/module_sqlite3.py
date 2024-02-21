import sqlite3


def main():
    connection = sqlite3.connect("my_db.db")
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Users ("
        "id INTEGER PRIMARY KEY,"
        "name TEXT NOT NULL,"
        "age INTEGER"
        ")"
    )
    # cursor.execute("INSERT INTO Users (name, age) VALUES (?, ?)", ("Vasya", 18))
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    print(users)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
