import sqlite3

def create_tables():
    conn.execute("DROP TABLE IF EXISTS students")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            city TEXT
        )
    """)

def add_student(name, age, city):
    conn.execute(
       "INSERT INTO students (name, age, city) VALUES (?, ?, ?)",
        (name, age, city)
    )
    conn.commit()

def delete_student(student_id):
    conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

def get_students():
    result = conn.execute("SELECT * FROM students ORDER BY age DESC, city LIMIT 2")
    return result

def get_student_by_age(age):
    result = conn.execute(
        "SELECT id, name FROM students WHERE age = ?",
        (age,)
    )
    return result


if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    create_tables()

    add_student("John", 20, "New York")
    add_student("Aibek", 22, "Karakol")
    add_student("Aisuluu", 19, "Karakol")
    add_student("Ariana", 19, "Bishkek")

    for st in get_students():
        print(st)
    print("----------------")

    # delete_student(1)

    for st in get_students():
        print(st)

    print("--------------")
    for st in get_student_by_age(20):
        print(st)
