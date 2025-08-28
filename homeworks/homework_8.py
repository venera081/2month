import sqlite3


def create_table():
    conn.execute("DROP TABLE IF EXISTS genres")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            genre_id TEXT,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    """)

def insert_genres(name: str):
    conn.execute(
        "INSERT INTO genres (name) VALUES (?)", (name,)
    )
    conn.commit()

def insert_books(name: str, author: str, publication_year: int, number_of_pages: int, number_of_copies: int,
                 genre_id: int):
    conn.execute(
        "INSERT INTO books (name, author, publication_year, number_of_pages, number_of_copies, genre_id)"
        "VALUES (?, ?, ?, ?, ?, ?)",
        (name, author, publication_year, number_of_pages, number_of_copies, genre_id)
    )
    conn.commit()

def delete_book(book_id):
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()

def get_books_with_genres():
    result = conn.execute(
        "SELECT * FROM books JOIN genres ON books.genre_id = genres.id"
    )
    return result

if __name__ == '__main__':
    conn = sqlite3.connect("database.db")
    create_table()

    insert_genres("Novel")
    insert_genres("Fantasy")
    insert_genres("Chinese classical literature")
    insert_genres("Adventure")
    insert_genres("Historical novel")



    insert_books("Don Quixote", "Miguel de Cervantes", 1605, 863,
                 500, 1)
    insert_books("A Tale of Two Cities", "Charles Dickens", 1859, 489,
                 200, 5)
    insert_books("The Lord of the Rings", "J.R.R. Tolkien", 1954, 1216,
                 150, 2)
    insert_books("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997,
                 223, 120, 2)
    insert_books("Dream of the Red Chamber", "Cao Xueqin", 1791,  2500,
                 100, 3)
    insert_books("She: A History of Adventure", "H. Rider Haggard", 1887, 317,
                 83, 4)
    insert_books("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 1950,
                 208, 85, 2)

    delete_book(6)


    for sw in get_books_with_genres():
        print(sw)

    conn.close()
