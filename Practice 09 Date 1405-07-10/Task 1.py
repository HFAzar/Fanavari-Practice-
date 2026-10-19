'''
     * In The Name Of God *
''' 
#              H
#             /|\
#            / | \
#           /--F--\
#          / \ | / \
#         *--- A ---*
#          \ / Z \ /
#           \  A  /
#            *-R-*
#             \ /
#          ====*=====
#          | HFAZAR |
#          ==========
'''
================================================
  Author         : HFAzar
  Project Title  : Grade Recording and Analysis System
  Class Session  : 09
  Level          : {level}
  Date           : 1405-07-10
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%
'''
Task number 01:

Description: Grade Recording and Analysis System

Try / Except · File Management · Functions
Suppose you are responsible for recording grades for a class. Write a program 
that takes student names and grades as input and saves them to a file named
`grades.txt`.
Each line in the file should follow this format:
Ali,18.5
Sara,16
Reza,19.25

Required Features:
1.	An `add_grade()` function to accept a student's name and grade and save 
them to the file.
2.	A `read_grades()` function to read and display the grades.
3.	A `calculate_average()` function to calculate the class average.
4.	A `find_top_student()` function to identify the student with the highest grade.
5.	Use `try/except` blocks to handle errors, such as entering text instead of
a numerical grade, grades outside the 0–20 range, missing files, or invalid data.
Bonus Challenge: Prevent multiple entries for the same student. If a new grade 
is entered for a student who is already in the system, update their existing grade.
'''
#%%
 

# ================================================
#   Task 1 — Grade Recording and Analysis System
# ================================================

# ---------- Helper Functions ----------

def load_grades():
    grades = {}
    try:
        with open("grades.txt", "r") as f:
            for line in f:
                try:
                    name, score = line.strip().split(",")
                    grades[name] = float(score)
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
    return grades


def save_grades(grades):
    with open("grades.txt", "w") as f:
        for name, score in grades.items():
            # Use :g to remove .0 from whole numbers (e.g., 16.0 -> 16)
            f.write(f"{name},{score:g}\n")


# ---------- Main Functions ----------

def add_grade():
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        score = float(input("Grade: "))
    except ValueError:
        print("The score must be a number.")
        return

    if not (0 <= score <= 20):
        print("Grade must be between 0 and 20.")
        return

    grades = load_grades()
    grades[name] = score  # Overwrites if the name exists (Bonus Challenge)
    save_grades(grades)
    print("Saved successfully.")


def read_grades():
    grades = load_grades()
    if not grades:
        print("No grades found.")
        return
    print("\n--- Grades ---")
    for name, score in grades.items():
        print(f"{name}: {score}")


def calculate_average():
    grades = load_grades()
    if not grades:
        print("No grades available to calculate average.")
        return
    
    avg = sum(grades.values()) / len(grades)
    print(f"Class Average: {avg:.2f}")


def find_top_student():
    grades = load_grades()
    if not grades:
        print("No grades found.")
        return

    top_name = max(grades, key=grades.get)
    print(f"Top Student: {top_name} with {grades[top_name]}")


# ---------- Main Menu ----------

if __name__ == "__main__":
    while True:
        print("\n--- Menu ---")
        print("1. Add Grade")
        print("2. Read Grades")
        print("3. Calculate Average")
        print("4. Find Top Student")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_grade()
        elif choice == "2":
            read_grades()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            find_top_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")








