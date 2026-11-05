# Module 1: Data Science Fundamentals Overview

print("=== 6. Data Science Concepts Practice ===")

# Sample Dataset Representation using Lists & Dictionaries
dataset = [
    {"id": 1, "score": 85, "passed": True},
    {"id": 2, "score": 42, "passed": False},
    {"id": 3, "score": 90, "passed": True},
    {"id": 4, "score": 78, "passed": True},
]

scores = [item["score"] for item in dataset]
avg_score = sum(scores) / len(scores)

print(f"Total Student Records: {len(dataset)}")
print(f"All Scores: {scores}")
print(f"Average Score: {avg_score:.2f}")

passed_students = [item for item in dataset if item["passed"]]
print(f"Passed Students Count: {len(passed_students)}")
