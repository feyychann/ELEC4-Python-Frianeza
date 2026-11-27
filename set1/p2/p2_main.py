# p2_main.py

# Name: FRIANEZA, MARIBEL F. 
# Section: IV BSIT B
# Date: November 27, 2026
# Activity: P2 Student Utils

# Import style 1:  it will only import the needed functions (call functions as function)
import student_utils

# Import style 2: import particular names directly
from student_utils import get_highest, get_lowest

# Built-in module: datetime for timestamping the report
from datetime import datetime


def read_grades():
    # Ask the user to enter grades and get a list of grades back.
    while True:
        try:
            count = int(input("How many grades you want to enter? "))
            if count > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    grades = []
    for i in range(1, count + 1):
        while True:
            try:
                grade = float(input(f"Enter grade the {i}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return grades


def main():
    print("=== Student Grade Report ===")
    grades = read_grades()

    # It uses import style 1 (module.function)
    average = student_utils.calculate_average(grades)
    status = student_utils.determine_pass_fail(average)

    # It uses import style 2 (name imported directly)
    highest = get_highest(grades)
    lowest = get_lowest(grades)

    # It uses the Built-in module in a meaningful way: report timestamp
    generated = datetime.now().strftime("%B %d, %Y %I:%M %p")

    print("\n--- Report ---")
    print(f"Grades entered : {grades}")
    print(f"Average        : {average:.2f}")
    print(f"Highest grade  : {highest}")
    print(f"Lowest grade   : {lowest}")
    print(f"Result         : {status}")
    print(f"Reported on: {generated}")


if __name__ == "__main__":
    main()