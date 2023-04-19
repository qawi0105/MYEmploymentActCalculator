#Here are some of the quantitative aspects of the Employment Act in Malaysia that can be expressed in mathematical terms

# Define a function to calculate basic rate of pay
def calculate_basic_rate():
    total_salary = float(input("Enter your total monthly salary: "))
    working_days = int(input("Enter the number of working days in the month: "))

    basic_rate = total_salary / working_days
    print("Your basic rate of pay is RM {:.2f} per day.".format(basic_rate))

# Define a function to calculate overtime pay
def calculate_overtime_pay():
    basic_rate = float(input("Enter your basic rate of pay: "))
    overtime_hours = int(input("Enter the number of hours worked overtime: "))

    overtime_rate = basic_rate * 1.5
    overtime_pay = overtime_rate * overtime_hours
    print("Your overtime pay is RM {:.2f}.".format(overtime_pay))

# Display options for the user to choose from
print("Welcome to the Employment Act Calculator!")
print("Please choose an option:")
print("1. Calculate basic rate of pay")
print("2. Calculate overtime pay")

# Get user input and call the appropriate function
option = int(input("Enter your choice (1 or 2): "))
if option == 1:
    calculate_basic_rate()
elif option == 2:
    calculate_overtime_pay()
else:
    print("Invalid option. Please try again.")
