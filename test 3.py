grade_book = {
    "Alice": 88,
    "Bob": 92,
    "Charlie": 75,
    "Diana": 95,
    "Ethan": 81
}

print("=== STUDENT GRADE BOOK ===\n")
print("Class Records:", grade_book)
print("-" * 30)

total_score = 0
for score in grade_book.values():
    total_score += score

class_average = total_score / len(grade_book)
print(f"Class Average Score: {class_average:.2f}")

highest_score = max(grade_book.values())
lowest_score = min(grade_book.values())

top_students = [name for name, score in grade_book.items() if score == highest_score]
bottom_students = [name for name, score in grade_book.items() if score == lowest_score]

print(f"Top Scorer(s): {', '.join(top_students)} with a score of {highest_score}")
print(f"Bottom Scorer(s): {', '.join(bottom_students)} with a score of {lowest_score}")
print("-" * 30)

search_name = input("Enter the name of the student you want to look up: ").strip()

student_score = grade_book.get(search_name)

if student_score is not None:
    print(f"Success! {search_name}'s score is: {student_score}")
else:
    print(f"Sorry, '{search_name}' was not found in the grade book.")
