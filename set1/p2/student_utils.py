# student_utils.py

PASSING_GRADE = 75  


def calculate_average(grades):
    """Return the average of a list of grades."""
    return sum(grades) / len(grades)


def determine_pass_fail(average):
    """Return 'Passed' if the average meets the passing grade, else 'Failed'."""
    return "Passed" if average >= PASSING_GRADE else "Failed"


def get_highest(grades):
    """Return the highest grade in the list."""
    return max(grades)


def get_lowest(grades):
    """Return the lowest grade in the list."""
    return min(grades)


# This code block will execute only when the file is executed directly (python student_utils.py) 
# and NOT when it is imported by some other script like p2_main.py.
if __name__ == "__main__":
    sample = [79, 80, 88, 83, 72]
    avg = calculate_average(sample)
    print("Testing student_utils.py\n")
    print ("This is the sample Grades:", sample)
    print("Average:", avg)
    print("Result:", determine_pass_fail(avg))
    print("Highest:", get_highest(sample))
    print("Lowest:", get_lowest(sample))