# Module 1: Loops & Conditional Statements Practice

print("=== 2. Conditionals & Loops ===")

# Conditional Statements
num = 15
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# For Loop
print("\nCounting 1 to 5 using For Loop:")
for i in range(1, 6):
    print(f"Number: {i}")

# While Loop
print("\nCountdown using While Loop:")
count = 3
while count > 0:
    print(f"Count: {count}")
    count -= 1
print("Loop completed!")
