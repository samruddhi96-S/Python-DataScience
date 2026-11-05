# Module 1: Functions Practice

print("=== 3. Functions ===")

def greet_user(user_name):
    return f"Hello, {user_name}! Welcome to Data Science Practice."

def calculate_square(number):
    return number ** 2

# Calling Functions
message = greet_user("Python Learner")
print(message)

num = 7
print(f"Square of {num} is {calculate_square(num)}")
