"""
Week 1 Activities - Li, Chenyang
"""
# 1. List 3 ways of collecting user input
# input()
# sys.stdin.read()
# fileinput.input()

# 2. Use one of them to collect two numbers and print the addition, subtraction, multiplication and division of them.
number_a = int(input("Please enter an integer:"))
number_b = int(input("Please enter a second integer:"))
print(f"{number_a} + {number_b} = {number_a + number_b}")
print(f"{number_a} - {number_b} = {number_a - number_b}")
print(f"{number_a} × {number_b} = {number_a * number_b}")
print(f"{number_a} ÷ {number_b} = {number_a / number_b}")
