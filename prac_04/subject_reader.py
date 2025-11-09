"""
Practical 04 - Lists
Subject Reader - Load subject data and display details
"""

# --------------------------------------------------
# Pseudocode
# --------------------------------------------------
# 1. Define a function load_subjects(filename):
#       - Open the given file for reading (using with)
#       - Create an empty list called subjects
#       - For each line in the file:
#             - Strip whitespace
#             - Split the line by commas into code, lecturer, students
#             - Convert students to int
#             - Append [code, lecturer, students] to subjects
#       - Return the subjects list
#
# 2. Define a function display_subjects(subjects):
#       - For each subject in subjects:
#             - Unpack into code, lecturer, students
#             - Print details in format:
#                 "{code} is taught by {lecturer} and has {students} students"
#
# 3. Define main():
#       - Call load_subjects("subject_data.txt")
#       - Call display_subjects(subjects)
#
# 4. Run main()



FILENAME = "subject_data.txt"


def main():
    """Read subject data and display it neatly."""
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename):
    """Load data from file and return a list of [code, lecturer, student_count]."""
    subjects = []
    with open(filename, "r") as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            code = parts[0]
            lecturer = parts[1]
            students = int(parts[2])
            subjects.append([code, lecturer, students])
    return subjects


def display_subjects(subjects):
    """Display subject details neatly formatted."""
    for code, lecturer, students in subjects:
        print(f"{code} is taught by {lecturer} and has {students} students")


main()
