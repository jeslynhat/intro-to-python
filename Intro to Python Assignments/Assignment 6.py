
# ASSIGNMENT 6 - Python Basics with datetime and functions
# This assignment uses script to show how to work with time, dates, and simple functions in Python.

# PROBLEM 1:
# Try the code below and revise it to current time:
# CODE GIVEN:
# import sys
#	for line in sys.stdin:
#		data = line.strip().split("\t")
#		if len(data) == 6:
#			date, time, store, item, cost, payment = data
#			print "{0}\t{1}".format(item, cost)

# MY WORK:
# CREATE FAKE LIST DATA FOR PYCHARM

# Step 1: Create a list of fake receipt lines
# Each line is a string with 6 parts separated by tabs (\t)
fake_data = [
    "2025-06-28\t12:00\tTarget\tToothpaste\t$2.99\tCard",
    "2025-06-28\t12:05\tWalmart\tNotebook\t$1.50\tCash",
    "2025-06-28\t12:10\tPublix\tBananas\t$0.99\tCard"
]

# Step 2: Loop through each line in the list
for line in fake_data:
# Step 3: Remove extra spaces and split the line into parts using tab (\t)
     data = line.strip().split("\t")

# Step 4: Check if the line has exactly 6 parts
     if len(data) ==6:     # Step 5: Next, unpack the parts into separate variables
          date, time, store, item, cost, payment = data
          print("{0}\t{1}".format(item, cost))     # Step 6: Print just the item and cost

print("")
print("")


# PROBLEM 2:
# Add the timedelta to the datetime and subtract 60 second and added 2 year.
# Hint: timedelta(seconds=60)) For each condition, state the code and output.

# CODE GIVEN:
# from datetime import datetime
# from datetime import timedelta
# (blank line)
# #Add 1 day
# print datetime.now() + timedelta(days=1)

# MY WORK:
# Step 1: Import the datetime and timedelta tools
from datetime import datetime, timedelta

# Step 2: Get the current time
now = datetime.now()
print("Current time:", now)

# Step 3: Add 1 day by using timedelta days
print("Add 1 day:", now + timedelta(days=1))

# Step 4: Subtract 60 Seconds by using timedelta seconds
print("Subtract 60 seconds:", now - timedelta(seconds=60))

# Step 5: Add 2 Years using days since there is not built-in years in timedelta
print("Add 2 years (730 days):", now + timedelta(days=730))


print("")
print("")

# Problem 3: Create a timedelta object representing 100 days, 10 hours, and 13 minutes.
# CODE GIVEN:
# >>> from datetime import timedelta
# >>> d = timedelta(microseconds=-1)
# >>> (d.days, d.seconds, d.microseconds)
# (-1, 86399, 999999)

# MY WORK:
# Step 1: Import timedelta if not already done (imported in Problem 2)
# Step 2: Create the timedelta Object using the timedelta function to set the time.

delta = timedelta(days=100, hours=10, minutes=13)
# Basically, this tells Python "Make a time duration that's 100 days, 10 hours, and 13 minutes long."

# Step 3: Print the result
print("Custom timedelta:", delta)

print("")
print("")

# Problem 4: Write a function that takes two arguments (feet and inches) with this time object.
# CODE GIVEN:
# from datetime import datetime
# get current date
#>>>datetime_object = datetime.now()
#>>>print(datetime_object)
#>>> print('Type :- ',type(datetime_object))

# MY WORK:
# Step 1: Import datetime if not already done (imported in Problem 2)
# Step 2: Define a function that takes two inputs: feet and inches
def process_measurement(feet, inches):
    current_time = datetime.now()
    print("Feet: {0}, Inches: {1}, Time {2}".format(feet, inches, current_time))
	
# Step 3: Call the function with the 5, 10 values
process_measurement(5, 10)
