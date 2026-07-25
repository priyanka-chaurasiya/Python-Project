# ==========================
# Quiz Game in Python
# ==========================

print("===== WELCOME TO PYTHON QUIZ GAME =====")

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used for Python programming?",
        "options": ["A. English", "B. Java", "C. Python", "D. C++"],
        "answer": "C"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "4. Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. display()", "D. output()"],
        "answer": "B"
    },
    {
        "question": "5. Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct Answer: {q['answer']}")

print("\n===== QUIZ COMPLETED =====")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print(" Excellent!")
elif percentage >= 60:
    print(" Good Job!")
else:
    print("Keep Practicing!")