from string import ascii_uppercase
try:
    print("Welcome to my Computer Quiz!")

    playing = input("Do you want to play?(Yes/No) ")

    if playing.lower() != "yes":
        quit()
    print("ok let's play!: ")
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "Berlin", "Rome", "Madrid"],
            "answer": "Paris",
            "difficulty": "Easy",
            "category": "Geography"
        },
        {
            "question": "Who developed the theory of relativity?",
            "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Stephen Hawking"],
            "answer": "Albert Einstein",
            "difficulty": "Medium",
            "category": "Science"
        },
        {
            "question": "What is the result of 7 * 8?",
            "options": ["54", "56", "64", "58"],
            "answer": "56",
            "difficulty": "Easy",
            "category": "Math"
        }
    ]
    num_of_questions = len(quiz_questions)
    correct_answers = 0
    i = 1
    for q in quiz_questions:
        print(f"{i}. {q["question"]}")
        i += 1
        for j, option in enumerate(q["options"]):
            print(f"    {ascii_uppercase[j]}. {option}")
        answer = input("Answer: ")
        if answer.lower() == q["answer"].lower():
            correct_answers += 1
            print("Correct!")
        elif answer.lower() in [o.lower() for o in q["options"]]:
            print("Your answer is wrong")
        else:
            print("Invalid answer")
        
    print(f"You got {correct_answers}/{num_of_questions} Answers correct!")
    print("Thank you for playing this game!")
except Exception as e:
    print(e)

