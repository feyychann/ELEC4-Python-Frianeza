#p3_record_manager.py

# Name: FRIANEZA, MARIBEL F. 
# Section: IV BSIT B
# Date: November 27, 2026
# Activity: P2 Student Utils


# Students: The list will store the name exactly as entered (to ensure proper display).
# seen_names:  A SET which contains all names but in lowercase form, useful only for checking duplication of names.
students = []
seen_names = set()


def normalize(name):
    # Clean a name so 'Maribel Frianeza', ' maribel frianeza' and 'MARIBEL FRIANEZA' match.
    return " ".join(name.split()).lower()


def add_student():
    name = " ".join(input("Enter student name to add: ").split())
    if name == "":
        print("Name cannot be empty.")
        return

    key = normalize(name)
    if key in seen_names:
        print(f"'{name}' already exists. Duplicate not added.")
        return

    students.append(name.title())
    seen_names.add(key)
    print(f"'{name.title()}' was added.")


def remove_student():
    name = input("Enter student name to remove: ")
    key = normalize(name)

    if key not in seen_names:
        print(f"'{name.strip()}' was not found.")
        return

    for student in students:
        if normalize(student) == key:
            students.remove(student)
            break
    seen_names.remove(key)
    print(f"'{name.strip().title()}' was removed.")


def search_student():
    term = normalize(input("Enter name or part of a name to search: "))
    if term == "":
        print("Please type something to search.")
        return

    matches = [s for s in sorted(students, key=normalize) if term in normalize(s)]

    if not matches:
        print("No matching students found.")
        return

    print(f"\nFound {len(matches)} match(es):")
    for number, student in enumerate(matches, start=1):
        print(f"  {number}. {student}")


def display_students():
    if not students:
        print("No students in the list yet.")
        return

    print("\n--- Student List (A-Z) ---")
    for number, student in enumerate(sorted(students, key=normalize), start=1):
        print(f"{number}. {student}")
    print(f"Total students: {len(students)}")


def show_menu():
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add student")
    print("2. Remove student")
    print("3. Search student")
    print("4. Display all students")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()

# EXPLANATION:
#In Python, a lists keep items in the order in which they are entered with duplicate items allowed, 
#whereas sets do not keep items in order, and duplicates are not allowed. 
#I have used a list (students) for storing the names because the program will need to show the names, 
#enumerate them, and sort them alphabetically. On the other hand, 
#I have used a set (seen_names) to store the lower case version of all the names entered 
#so far to check for duplicity instantly in case the same name is entered as "maribel frianeza" or "MARIBEL FRIANEZA".

