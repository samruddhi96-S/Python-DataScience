# Module 1: Variables & Data Types Practice

print("=== 1. Variables & Data Types ===")

name = "Intern"
age = 22
gpa = 3.8
is_enrolled = True

print(f"Name: {name} (Type: {type(name).__name__})")
print(f"Age: {age} (Type: {type(age).__name__})")
print(f"GPA: {gpa} (Type: {type(gpa).__name__})")
print(f"Enrolled: {is_enrolled} (Type: {type(is_enrolled).__name__})")

# Type Casting Example
age_str = str(age)
print(f"Converted Age to String: '{age_str}'")
