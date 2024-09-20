# Activity 1
# Set Aliasing
# Original set
original_set = {1, 2, 3}

# Alias to the original set
alias_set = original_set

# Modifying the alias set
alias_set.add(4)

# Both sets reflect the change
print("Original Set:", original_set)  # Output: {1, 2, 3, 4}
print("Alias Set:", alias_set)  # Output: {1, 2, 3, 4}

# Activity 2
# Difference between extend and append in python
"""append: Adds its argument as a single element to the end of a list. The length of the list increases by one.
extend: Iterates over its argument, adding each element to the list, extending the list."""
# Using append
list1 = [1, 2, 3]
list1.append([4, 5])
print("After append:", list1)  # Output: [1, 2, 3, [4, 5]]

# Using extend
list2 = [1, 2, 3]
list2.extend([4, 5])
print("After extend:", list2)  # Output: [1, 2, 3, 4, 5]

# Activity 3
# Tell a number is positive, negative or zero without using elif
number = 5  # Change this value to test different cases

if number < 0:
    print("The number is negative")
else:
    if number == 0:
        print("The number is zero")
    else:
        print("The number is positive")

# Activity 4
# Write a program to add and query student grades
student_grades = {}


def add_student_grade(name, grade):
    """Add the grade for a student if they do not already exist."""
    if name in student_grades:
        print(f"Student {name} already exists. Grade not updated.")
    else:
        student_grades[name] = grade
        print(f"Grade for {name} has been set to {grade}.")


def query_student_grade(name):
    """Query the grade of a student."""
    grade = student_grades.get(name)
    if grade is not None:
        print(f"{name} has a grade of {grade}.")
    else:
        print(f"No grade found for {name}.")


def main():
    while True:
        print("\nOptions:")
        print("1. Add Student Grade")
        print("2. Query Student Grade")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student_grade(name, grade)
        elif choice == '2':
            name = input("Enter student name to query: ")
            query_student_grade(name)
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# Activity 5
# To write code to demonstrate the difference between global and local variables
# Global variable
global_var = "I am a global variable"


def my_function():
    # Local variable
    local_var = "I am a local variable"
    print(local_var)  # This will print the local variable
    print(global_var)  # This will print the global variable


my_function()

# Trying to print the local variable outside the function will cause an error
# print(local_var)  # Uncommenting this line will raise a NameError

# Global variable can be accessed outside the function
print(global_var)

# Activity 6
# To write code to demonstrate the use of global keyword
# Global variable
var = "I am a global variable"


def my_function():
    # Local variable with the same name as the global variable
    var = "I am a local variable"
    print("Inside the function:", var)  # This will print the local variable


def change_global_var():
    global var  # Declare that we are using the global variable
    var = "I have been changed globally"
    print("Inside change_global_var function:",
          var)  # This will print the changed global variable


print("Before calling any function:",
      var)  # This will print the global variable
my_function()
print("After calling my_function:",
      var)  # This will still print the global variable
change_global_var()
print("After calling change_global_var:",
      var)  # This will print the changed global variable


# Activity 7
# To write code based on object-oriented programming concepts
# Define the Student class
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_student(self):
        print(f"Student {self.name} has a grade of {self.grade}.")


# Dictionary to store student names and Student objects
student_grades = {}


def add_student_grade(name, grade):
    """Add the grade for a student if they do not already exist."""
    if name in student_grades:
        print(f"Student {name} already exists. Grade not updated.")
    else:
        student_grades[name] = Student(name, grade)
        print(f"Grade for {name} has been set to {grade}.")


def query_student_grade(name):
    """Query the grade of a student."""
    student = student_grades.get(name)
    if student is not None:
        student.display_student()
    else:
        print(f"No grade found for {name}.")


def main():
    while True:
        print("\nOptions:")
        print("1. Add Student Grade")
        print("2. Query Student Grade")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student_grade(name, grade)
        elif choice == '2':
            name = input("Enter student name to query: ")
            query_student_grade(name)
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
