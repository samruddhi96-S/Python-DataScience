# Module 1: File Handling Practice

print("=== 5. File Handling ===")

filename = "sample.txt"

# Writing to a file
with open(filename, "w", encoding="utf-8") as file:
    file.write("Hello! Yeh file handling ka demo hai.\n")
    file.write("Python & Data Science Fundamentals Practice completed.\n")

print(f"Data successfully written to '{filename}'.")

# Reading from a file
print("\nReading contents of file:")
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
