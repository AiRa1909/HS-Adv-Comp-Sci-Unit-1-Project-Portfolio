import sqlite3
#import the sqlite 3 database.

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
    conn.execute("DELETE FROM cards")
    # clear all cards from past user sessions so that everyone gets the console program fresh
    conn.commit()
    return conn

def add_cards(conn):
    print("Let's add a card: ")
    question = input("Type the prompt here: ")
    answer = input("Type the answer here: ")

    if question and answer:
        conn.execute("INSERT INTO cards VALUES (?,?)", (question,answer))
        # the ? ? are placeholders for question and answer.
        conn.commit()
        print("\n Card added!")
    else:
        print("Please don't leave your prompt and answer empty!")
        #foolproofing our code haha so that people won't encounter an error or add something empty
        add_cards(conn)
def study_cards(conn):
    cursor = conn.execute("SELECT question, answer FROM cards")
    cards = cursor.fetchall()
    # we want to get ALL the cards from the question and answer columns

    if not cards:
        print("\n oops! Look like you need to go back and add some cards because we don't have any!")
        #more foolproofing so that people can't run a study session without cards
        return

    print("/n ----- LET'S STUDY ----- ")
    for question,answer in cards:
        print(f"Prompt: {question}")
        input("(press Enter for answer)")
        print(f"Answer: {answer}")
        print("\n Let's study the next; ")

def main():
    conn = setup_database()
    while True:
        print("Welcome to Flashcards Console Program!")
        print("PRESS 1. Add card")
        print("PRESS 2. Study cards")
        print("PRESS 3. Exit")

        choice = input("Choose: ").strip()
        # strip for precautions and more foolproofing

        if choice == "1":
            add_cards(conn)
        elif choice == "2":
            study_cards(conn)
        elif choice == "3":
            print("Oh well! Goodbye.")
            conn.close()
            break
        else:
            print("Please choose one of the given options!!!")
        #provide users with the seperate options of what they want to do. This will appear after every option has completed (every function of the three options or closing the connection)

if __name__ == "__main__":
    main()
