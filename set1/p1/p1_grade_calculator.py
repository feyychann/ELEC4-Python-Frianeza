#p1_grade_calculator.py


# Name: FRIANEZA, MARIBEL F. 
# Section: IV BSIT B
# Date: November 27, 2026
# Activity: P1 Student Grade Calculator



# Global variables: defined outside any function, so every function can see them.
PASSING_AVERAGE = 75
grades = []


# ---------------------------------------------------------------------------
# Function computation: it takes grades as an argument and returns some value. 
# They do not display anything.
# ---------------------------------------------------------------------------
def compute_average(grade_list):
    #Return the average of the grades.
    total = sum(grade_list)
    return total / len(grade_list)


def get_highest(grade_list):
    #Return the highest grade.
    return max(grade_list)


def get_lowest(grade_list):
    #Return the lowest grade.
    return min(grade_list)


def get_status(grade_list):
    #Return 'PASSED' if the average is at least the passing average, else 'FAILED'.
    if compute_average(grade_list) >= PASSING_AVERAGE:
        return "PASSED"
    return "FAILED"


# ---------------------------------------------------------------------------
# Input and menu functions
# ---------------------------------------------------------------------------
def get_valid_grade(prompt):
    #Keep asking until the user types a number from 0 to 100, then return it.
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("  Invalid input. Please enter a number from 0 to 100.")
            continue
        if 0 <= value <= 100:
            return value
        print("  Invalid grade. It must be from 0 to 100.")


def enter_grades(grade_list):
    #Replace the stored grades with new ones typed by the user.
    grade_list.clear()
    print("\nEnter the student's grades one at a time.")
    while True:
        grade = get_valid_grade(f"  Grade #{len(grade_list) + 1}: ")
        grade_list.append(grade)
        more = input("  Add another grade? (y/n): ").strip().lower()
        while more not in ("y", "n"):
            more = input(" Just type y or n: ").strip().lower()
        if more == "n":
            break
    print(f"Saved {len(grade_list)} grade(s).")


def view_results(grade_list):
    #Display the computed results (printing is done here, not in the computing functions).
    if not grade_list:
        print("\nNo grades entered yet. Choose option 1 first.")
        return
    print("\n--- Results ---")
    print("Grades  :", ", ".join(f"{g:g}" for g in grade_list))
    print(f"Average : {compute_average(grade_list):.2f}")
    print(f"Highest : {get_highest(grade_list):g}")
    print(f"Lowest  : {get_lowest(grade_list):g}")
    print(f"Status  : {get_status(grade_list)} (passing average is {PASSING_AVERAGE})")



def main():
    #Run the menu loop until the user chooses to exit.
    while True:
        #Print the main menu.
        print("\n===== GRADE CALCULATOR =====")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")
        
        choice = input("Select an option (1, 2 or 3): ").strip()
        if choice == "1":
            enter_grades(grades)
        elif choice == "2":
            view_results(grades)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()


# Global versus Local Variables:
# A global variable is defined outside of any function and can be used anywhere in the file; 
# for example, PASSING_AVERAGE and grades in this script. 
# A local variable is defined within a function and is only available within the scope of that function; 
# for example, total in compute_average() and the variable in get_valid_grade(). 
# If I were to try to print total outside of the function compute_average(), 
# Python will give a NameError since it is a local variable. However, global variables are good 
# for defining values that are common to the whole program, such as the passing mark.
