import sqlite3


def create_table():
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

def insert_books(name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute(
        "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)"
        "VALUES (?, ?, ?, ?, ?, ?)",
        (name, author, publication_year, genre, number_of_pages, number_of_copies)
    )
    conn.commit()

def delete_book(book_name):
    conn.execute("DELETE FROM books WHERE name = ?", (book_name,))
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect("database.db")
    create_table()

    insert_books("Don Quixote", "Miguel de Cervantes", 1605, "Novel",
                 863, 500)
    insert_books("A Tale of Two Cities", "Charles Dickens", 1859, "Historical Fiction",
                 489, 200)
    insert_books("The Lord of the Rings", "J.R.R. Tolkien", 1954, "Fantasy",
                 1216, 150)
    insert_books("The Little Prince", "Antoine de Saint-Exupéry", 1943, "Fable",
                 96, 140)
    insert_books("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997,
                 "Fantasy", 223, 120)
    insert_books("And Then There Were None", "Agatha Christie", 1939, "Mystery",
                 272, 100)
    insert_books("Dream of the Red Chamber", "Cao Xueqin", 1791,
                 "Classic Chinese Novel", 2500, 100)
    insert_books("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy",
                 310, 100)
    insert_books("She: A History of Adventure", "H. Rider Haggard", 1887, "Adventure",
                 317, 83)
    insert_books("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 1950, "Fantasy",
                 208, 85)

    delete_book("She: A History of Adventure")








