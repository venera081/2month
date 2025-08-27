import sqlite3

def create_tables():
    conn.execute("DROP TABLE IF EXISTS authors")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price INTEGER,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
    """)

def add_author(name: str):
    conn.execute("INSERT INTO authors (name) VALUES (?)", (name,))
    conn.commit()

def add_book(title: str, price: int, author_id: int):
    conn.execute(
        "INSERT INTO books (title, price, author_id) VALUES (?, ?, ?)",
        (title, price, author_id),
    )
    conn.commit()

def get_books_with_author():
    result = conn.execute(
        "SELECT * FROM books JOIN authors ON authors.id = books.author_id"
    )
    return result

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    create_tables()


    add_author('Абай Кунанбаев')
    add_author('Лев Толстой')
    add_author('Мухтар Ауэзов')
    add_author('Агата Кристи')
    add_author('Иван Тургенев')

    add_book('Слова назидания', 1000, 1)
    add_book('Путь Абая', 1500, 1)
    add_book( 'Война и мир', 2000, 2)
    add_book( 'Анна Каренина', 2500, 2)
    add_book( 'Лихая година', 3000, 3)
    add_book( 'Убийство в Восточном экспрессе', 4000, 4)
    add_book( 'Таинственное происшествие в Стайлзе', 4500, 4)
    add_book( 'Десять негритят', 5000, 4)
    add_book( 'Книга без автора', 2000, None)


    for d in get_books_with_author():
        print(d)

    conn.close()