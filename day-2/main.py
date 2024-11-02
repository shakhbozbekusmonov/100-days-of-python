
# Task 1 -- Solution
"""
two_digit_number = input("Type a two-digit number: >>> ")

input() function value by default string type.
Type Convertion: str to int

a = int(two_digit_number[0])
b = int(two_digit_number[1])
result = a + b

print(result)
"""

# Task 2 -- Solution
"""
height = input("Enter your height in m: >>> ")
weight = input("Enter your weight in kg: >>> ")

h = float(height)
w = int(weight)

bmi = int(w / (h ** 2))

print("Your BMI:", bmi)
"""

# Task 3 -- Solution
"""
age = input("What is your current age? >>> ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)
"""

# Task 4 -- Solution
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? >>> $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? >>> "))
people = int(input("How many people to split the bill? >>> "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)

message = f"Each person should pay: ${final_amount}"
print(message)
