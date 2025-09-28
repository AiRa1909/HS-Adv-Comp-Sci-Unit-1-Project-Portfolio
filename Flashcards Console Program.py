import sqlite3
import os

def setup_database():
    conn = sqlite3.connect("flashcards.db")
    # create database to store data
    conn.execute('''
    CREATE TABLE IF NOT EXISTS cards (
    question TEXT, 
    answer TEXT
    )
    ''')
    # making a database table with columns question and answer
    conn.commit()
    return conn

def add_cards(conn):
    print("Let's add a card: ")
    question = input("Type the question here: ")
    answer = input("Type the answer here: ")
    #some sql will come here later
    print("\n Card added!")

def study_cards(conn):
    #sql
    print("/n ----- LET'S STUDY ----- ")
    for question,answer in cards:
        print(f"Question: {question}")
        input("(press Enter for answer)")
        print(f"Answer: {answer}")
        print("\n You got it! That's correct")

def main():
    conn = setup_database()
    while True:
        print("Welcome to Flashcards Console Program!")
        print("PRESS 1. Add card")
        print("PRESS 2. Study cards")
        print("PRESS 3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_cards(conn)
        elif choice == "2":
            study_cards(conn)
        elif choice == "3":
            print("Oh well! Goodbye.")
            conn.close()
            break

if __name__ == "__main__":
    main()
