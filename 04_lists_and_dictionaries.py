# Module 1: Lists & Dictionaries Practice

print("=== 4. Lists & Dictionaries ===")

# Working with Lists
skills = ["Python", "Data Analysis", "Machine Learning", "SQL"]
skills.append("Git & GitHub")

print("Skills List:")
for idx, skill in enumerate(skills, start=1):
    print(f"{idx}. {skill}")

# Working with Dictionaries
student_profile = {
    "name": "Alex",
    "course": "Python & Data Science",
    "status": "In Progress",
    "completed_modules": 1
}

print("\nStudent Profile:")
for key, value in student_profile.items():
    print(f" - {key.capitalize()}: {value}")
