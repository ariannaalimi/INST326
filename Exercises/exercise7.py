"""A template for a python script deliverable for INST326.
Driver: Arianna Alimi
Navigator: None
Assignment: Exercise 7
Date: 11_20_24
Challenges Encountered: The close statements and the create_table method
"""

import sqlite3

#intitlaizing "library.db" to database
database = 'library.db'

#creating a table named books
books = """CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT, 
            author TEXT, 
            year_published INT, 
            genre TEXT
        );"""

#creating a table
#with each function, I use a with statement, automatically closing the connection,
#this means I do not need to use the close() command, or else it brings errors
def create_table():
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            cursor.execute(books) #executes the books table
            conn.commit()
    except sqlite3.Error as e: #except if can not create
        print ("Failed to create table:", e)


def add_book(title, author, year_published, genre):
    try:
        with sqlite3.connect(database) as conn:
            #used SQLite Python website to help 
            sql = '''INSERT INTO books(title, author, year_published, genre)
                    VALUES(?,?,?,?)''' 
            
            cursor = conn.cursor()
            cursor.execute(sql, (title, author, year_published, genre)) #executes command
            conn.commit()

    except sqlite3.Error as e: #if error, prints failed to add book
        print("Failed to add book:", e)

def view_books():
    try:
        with sqlite3.connect(database) as conn:
            
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM books')
            rows = cursor.fetchall() #used this command from SQLite Python website, fetches all rows
            return rows #returns rows as tuples
        

    except sqlite3.Error as e: #if error, prints failed to view book
        print("Failed to view books:", e)

def update_book(id, title, author, year_published, genre):
    
    #ChatGPT to help with error handling set up
    if not isinstance(id, int) or not id <= 0: #if ID is not an int or not greater than 0, invalid
            print("Invalid book ID.")
            return
    
    if not isinstance(year_published, int) or year_published <= 0: #if year published is not int or greater than 0, invalid
        print("Invalid year")
        return
    
    if not title or not author or not year_published or not genre: #if did not input needed arguments, invalid
        print("Title, author, year_published, or genre must be filled")
        return


    try:
        with sqlite3.connect(database) as conn:
            
            #updates information (title, author, year, genre) based on the ID
            update = 'UPDATE books SET title= ?, author= ?, year_published= ?, genre= ? WHERE id = ?'
            cursor = conn.cursor()
            cursor.execute(update, (title, author, year_published, genre, id))
            conn.commit()

    except sqlite3.Error as e: #if error, prints failed to update books
        print("Failed to update books:", e)

def delete_book(id):
    if not isinstance(id, int) or id <= 0: #if id is not int or greater than 0, invalid
            print("Invalid book ID.")
            return
    
    try:
        with sqlite3.connect(database) as conn:  
            delete = 'DELETE FROM books WHERE id = ?' #delete book based on ID
            cursor = conn.cursor()
            cursor.execute(delete, (id))
            conn.commit()

    except sqlite3.Error as e: #if error, prints failed to delete book
        print("Failed to delete books:", e)

#main function to test if the functions run
def main():
    create_table()
    add_book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
    add_book("1984", "George Orwell", 1949, "Dystopian")
    print(view_books())
    update_book(1, "To Kill a Mockingbird", "Harper Lee", 1960, "Classic Fiction")
    print(view_books())
    delete_book(2)
    print(view_books())

if __name__ == "__main__":
    main()