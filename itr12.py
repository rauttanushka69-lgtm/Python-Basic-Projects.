
#Question 1
def analyze_string(s):
    vowels = "aeiouAEIOU"

    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    space_count = 0

    for ch in s:
        if ch in vowels:
            vowel_count += 1
        elif ch.isalpha():
            consonant_count += 1
        elif ch.isdigit():
            digit_count += 1
        elif ch.isspace():
            space_count += 1

    print("\nString Analysis")
    print("----------------")
    print("Original String :", s)
    print("Length          :", len(s))
    print("Vowels          :", vowel_count)
    print("Consonants      :", consonant_count)
    print("Digits          :", digit_count)
    print("Spaces          :", space_count)


text = input("Enter a string: ")
analyze_string(text)




Function to analyze a string

def analyze_string(s):
    # Print length
    print("\nLength of the string:", len(s))

    # Print reverse string
    print("Reverse of the string:", s[::-1])

    # Count vowels (case insensitive)
    vowels = "aeiou"
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1

    print("Number of vowels:", count)

    # Print each character with positive and negative index
    print("\nCharacter\tPositive Index\tNegative Index")
    for i in range(len(s)):
        print(f"{s[i]}\t\t{i}\t\t{i - len(s)}")


# Main Program
user_string = input("Enter a string: ")

if user_string == "":
    print("Error: Empty string is not allowed.")
else:
    analyze_string(user_string)




#Question 2
# Function to manage student marks
def manage_marks():
    marks = []  # Empty list to store marks

    print("Enter marks for 5 subjects:")

    # Loop to take 5 subject marks
    for i in range(5):
        while True:
            try:
                # Take input and convert it to float
                mark = float(input(f"Enter marks for Subject {i + 1}: "))

                # Add mark to the list
                marks.append(mark)
                break

            except ValueError:
                # Handle non-numeric input
                print("Invalid input! Please enter numeric marks only.")

    # Calculate average marks
    average = sum(marks) / len(marks)

    # Find highest and lowest marks
    highest = max(marks)
    lowest = min(marks)

    # Sort marks in descending order
    marks.sort(reverse=True)

    # Display the results
    print("\n----- Result -----")
    print("Marks List:", marks)
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)


# Call the function
manage_marks()



#Question 3
# Class to represent a Student
class Student:

    # Constructor to initialize student details
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    # Method to add marks with validation
    def add_mark(self, mark):
        try:
            mark = float(mark)

            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")

            self.marks_list.append(mark)

        except ValueError as e:
            print("Invalid Input:", e)

    # Method to calculate average
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    # Method to display student information
    def display_info(self):
        print("\n----- Student Details -----")
        print("Name :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks :", self.marks_list)
        print("Average :", self.get_average())


# Main Program
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

student = Student(name, roll)

print("\nEnter 5 Marks:")

for i in range(5):
    mark = input(f"Mark {i+1}: ")
    student.add_mark(mark)

student.display_info()



#Question 4

# Function to manage student database
def student_database():

    students = {}

    while True:

        print("\n===== Student Database Menu =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":

                roll = input("Enter Roll Number: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

                print("Student Added Successfully.")

            elif choice == "2":

                roll = input("Enter Roll Number: ")

                record = students.get(roll)

                if record:
                    print(record)
                else:
                    print("Student Not Found.")

            elif choice == "3":

                if not students:
                    print("No Records Found.")

                else:
                    print("\nStudent Records")

                    for roll, info in students.items():
                        print("Roll:", roll)
                        print("Name:", info["Name"])
                        print("Age:", info["Age"])
                        print("City:", info["City"])
                        print("----------------------")

            elif choice == "4":
                print("Thank You!")
                break

            else:
                print("Invalid Choice.")

        except ValueError:
            print("Please enter valid input.")


# Function Call
student_database()



#Question 5

import random
import math

try:

    numbers = set()

    print("Enter 10 numbers:")

    # Input numbers
    for i in range(10):
        num = int(input(f"Number {i+1}: "))
        numbers.add(num)

    # Convert set to tuple
    numbers_tuple = tuple(numbers)

    print("\nUnique Numbers:", numbers)
    print("Tuple:", numbers_tuple)

    # Pick 3 random numbers
    if len(numbers_tuple) >= 3:
        random_numbers = random.sample(numbers_tuple, 3)
        print("3 Random Numbers:", random_numbers)
    else:
        print("Less than 3 unique numbers available.")

    # Calculate square root of sum
    total = sum(numbers_tuple)

    if total >= 0:
        print("Square Root of Sum:", math.sqrt(total))
    else:
        print("Square root cannot be calculated for negative sum.")

except ValueError:
    print("Please enter valid integer numbers.")

except Exception as e:
    print("Error:", e)



# Question 6
# Lambda function to calculate square
square = lambda x: x * x

try:
    # Generate numbers from 1 to 20
    numbers = range(1, 21)

    # Store squares in a list
    squares = [square(num) for num in numbers]

    print("Squares of numbers from 1 to 20:")
    print(squares)

    # Print only even squares
    print("\nEven Squares:")
    for value in squares:
        if value % 2 == 0:
            print(value, end=" ")

except Exception as e:
    print("Error:", e)



#Question 8
# Employee Class
class Employee:

    # Constructor
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)

    # Method to display employee details
    def show_details(self):
        print("-----------------------------")
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Department  :", self.details[0])
        print("Salary      :", self.details[1])


# Dictionary to store Employee objects
employees = {}

# Add 3 employees
for i in range(3):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")

    while True:
        try:
            salary = float(input("Enter Salary: "))
            break
        except ValueError:
            print("Invalid salary. Enter numeric value.")

    employees[emp_id] = Employee(emp_id, name, department, salary)

# Display all employees
print("\nEmployee Details")
for emp in employees.values():
    emp.show_details()



#Question 9
import math

try:
    # Take sentence input
    sentence = input("Enter a sentence: ")

    # Extract unique words
    words = set(sentence.lower().split())

    # Print unique words in sorted order
    print("\nUnique Words:")
    for word in sorted(words):
        print(word)

    # Count unique words
    count = len(words)

    Print square using math module
    print("\nSquare of total unique words:", math.pow(count, 2))

except Exception as e:
    print("Error:", e)



#question 10

import math
import random
from datetime import datetime

# Dictionary to store history
history = {}

# Function for arithmetic operations
def arithmetic():
    try:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose Operation: ")

        if choice == "1":
            return a + b
        elif choice == "2":
            return a - b
        elif choice == "3":
            return a * b
        elif choice == "4":
            return a / b
        else:
            print("Invalid Choice")
            return None

    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid Input.")

# Function for scientific calculation
def scientific():
    try:
        num = float(input("Enter Number: "))
        print("Square Root:", math.sqrt(num))
        print("Power (Square):", math.pow(num, 2))
        print("Factorial:", math.factorial(int(num)))
    except Exception as e:
        print("Error:", e)

# Function for random numbers
def random_numbers():
    print("Random Number:", random.randint(1, 100))

# Main Menu
while True:

    print("\n===== Smart Calculator =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Generate Random Number")
    print("4. Store Result")
    print("5. View History")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        result = arithmetic()
        if result is not None:
            print("Result:", result)

    elif choice == "2":
        scientific()

    elif choice == "3":
        random_numbers()

    elif choice == "4":
        value = input("Enter Result to Store: ")
        timestamp = str(datetime.now())
        history[timestamp] = value
        print("Result Stored Successfully.")

    elif choice == "5":
        print("\nHistory")
        for time, value in history.items():
            print(time, ":", value)

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")