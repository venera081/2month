import sqlite3

def create_tables():
    conn.execute("DROP TABLE IF EXISTS students")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            city TEXT REFERENCES
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

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    create_tables()

    add_student("John", 20, "New York")
    add_student("Aibek", 22, "Karakol")

    delete_student(1)