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

def view_cards(conn):
    cursor = conn.execute("SELECT question,answer FROM cards")
    cards = cursor.fetchall()

    if not cards:
        print("\n oops! Look like you need to go back and add some cards because we don't have any!")
        #more foolproofing so that people can't run a study session without cards
        return

    space = " "
    print(f"\n{space:>9}PROMPT {space:<4}ANSWER")
    for question,answer in cards:
        print(f"{space:>9}{question} {space:<4}{answer}")

def add_cards(conn):
    print("\n Let's add a card: ")
    question = input("Type the prompt here: ").strip().lower()
    answer = input("Type the answer here: ").strip().lower()

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

    print("\n ----- LET'S STUDY ----- ")
    for question,answer in cards:
        print(f"Prompt: {question}")
        study = input("(press Enter or type your answer)").lower().strip()
        user_pass = ""
        if study == user_pass:
            print(f"Answer: {answer}")
        elif study == answer:
            print("You got it right!")
        else:
            print("Looks like you got it wrong! Let's move on anyway; ")

    print("Out of cards! Exiting Quiz mode...")

def main():
    conn = setup_database()
    print("\n Welcome to the Flashcard Marker Console Program!")
    while True:
        print("\n PRESS 1. Add card")
        print("PRESS 2. Study cards")
        print("PRESS 3. Exit")

        choice = input("Choose: ").strip()
        # strip for precautions and more foolproofing

        if choice == "1":
            no_cards = int(input("How many cards would you like to add? "))
            for i in range(no_cards):
                add_cards(conn)
        elif choice == "2":
            choice = int(input("View 1: all flashcards or go into 2: Quiz Mode? "))
            if choice == 1:
                view_cards(conn)
            elif choice == 2:
                study_cards(conn)
            else:
                print("Please go back and choose a valid option! ")
                main()
        elif choice == "3":
            print("Oh well! Goodbye.")
            conn.close()
            break
        else:
            print("Please choose one of the given options!!!")
        #provide users with the seperate options of what they want to do. This will appear after every option has completed (every function of the three options or closing the connection)

if __name__ == "__main__":
    main()
