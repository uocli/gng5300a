# Generate Hello World with Copilot.
print("Hello, World!")

# Ask Copilot to generate code for counting the number of characters in my name.
name = "Chenyang"
char_count = len(name)
print(f"The number of characters in the name '{name}' is {char_count}.")

# Takes two numbers as input and prints the division of the two numbers.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of dividing {num1} by {num2} is {result}.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")

# Ask Copilot to generate code for collecting the user inputs as numbers and add them into a predefined list until a stop sign is given.
numbers = []
while True:
    user_input = input(
        "Enter a number to add to the list (or type 'stop' to finish): ")
    if user_input.lower() == 'stop':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Error: Please enter a valid number.")
print("The numbers in the list are:", numbers)

# Write a program that asks for a student's name and then prints the student's grade.
students_grades = {
    "Alice": "A",
    "Bob": "B",
    "Cean": "A+",
    "David": "C",
    "Eva": "B+"
}

student_name = input("Enter the student's name: ")
grade = students_grades.get(student_name, "Student not found.")
print(f"The grade for {student_name} is {grade}.")
