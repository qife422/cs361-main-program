import os
import time

NOTES_FILE = "notes.txt"

def print_header(title):
    print("\n" + "+" + "-" * 50 + "+")
    print("|" + title.center(50) + "|")
    print("+" + "-" * 50 + "+")

def framed_print(text):
    lines = text.strip().split("\n")
    print("+" + "-" * 50 + "+")
    for line in lines:
        print("| " + line.ljust(48) + " |")
    print("+" + "-" * 50 + "+")

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as file:
        lines = file.readlines()
    notes = []
    for line in lines:
        parts = line.strip().split("||")
        if len(parts) == 3:
            title, content, timestamp = parts
            notes.append({"title": title, "content": content, "timestamp": timestamp})
    return notes

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        for note in notes:
            file.write(f"{note['title']}||{note['content']}||{note['timestamp']}\n")

def create_note():
    print_header("Create Note")
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    timestamp = time.ctime()
    notes = load_notes()
    notes.append({"title": title, "content": content, "timestamp": timestamp})
    save_notes(notes)
    framed_print("Note created successfully.")

def edit_note(note, notes):
    print_header("Edit Note")
    new_title = input(f"Enter new title (or press Enter to keep '{note['title']}'): ").strip()
    new_content = input("Enter new content (or press Enter to keep existing content): ").strip()
    if new_title:
        note['title'] = new_title
    if new_content:
        note['content'] = new_content
    note['timestamp'] = time.ctime()
    save_notes(notes)
    framed_print("Note updated successfully.")

def view_notes():
    print_header("View Notes")
    notes = load_notes()
    if not notes:
        framed_print("No notes available.")
        return
    for idx, note in enumerate(notes):
        print(f"{idx + 1}. {note['title']} (Last Modified: {note['timestamp']})")
    choice = input("Enter the number of the note to view or 'b' to go back: ")
    if choice.lower() == 'b':
        return
    try:
        index = int(choice) - 1
        note = notes[index]
        print_header("Note Detail")
        framed_print(f"Title: {note['title']}\nContent: {note['content']}\nLast Modified: {note['timestamp']}")
        edit_choice = input("Would you like to edit this note? (y/n): ").lower()
        if edit_choice == 'y':
            edit_note(note, notes)
    except (IndexError, ValueError):
        framed_print("Invalid choice.")

def search_notes():
    print_header("Search Notes")
    keyword = input("Enter keyword to search in notes: ").lower()
    notes = load_notes()
    matches = [note for note in notes if keyword in note['title'].lower() or keyword in note['content'].lower()]
    if not matches:
        framed_print("No matching notes found.")
        return
    print(f"Found {len(matches)} matching notes:")
    for idx, note in enumerate(matches):
        print(f"{idx + 1}. {note['title']} (Last Modified: {note['timestamp']})")
    choice = input("Enter the number of the note to view or 'b' to go back: ")
    if choice.lower() == 'b':
        return
    try:
        index = int(choice) - 1
        note = matches[index]
        print_header("Note Detail")
        framed_print(f"Title: {note['title']}\nContent: {note['content']}\nLast Modified: {note['timestamp']}")
        edit_choice = input("Would you like to edit this note? (y/n): ").lower()
        if edit_choice == 'y':
            all_notes = load_notes()
            for n in all_notes:
                if n['title'] == note['title'] and n['timestamp'] == note['timestamp']:
                    edit_note(n, all_notes)
                    break
    except (IndexError, ValueError):
        framed_print("Invalid choice.")

def main():
    while True:
        print_header("Home Page")
        print("1. Create Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            framed_print("Goodbye!")
            break
        else:
            framed_print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

