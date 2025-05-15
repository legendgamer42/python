import random
import time

operators = ["+", "-", "*"]

while True:
    total_problems = input("How many math problems do you want? ")
    if total_problems.isdigit():
        total_problems = int(total_problems)
        break
    else:
        print("Must be a Number!")


def generate_problem():
    left_operand = random.randint(1,20)
    right_operand = random.randint(1,20)
    operator = random.choice(operators)

    expr = str(left_operand) + operator + str(right_operand)

    answer = int(eval(f'{expr}'))
    return expr, answer
generate_problem()
score = 0
wrong_answers = []
input("Press enter to start")
print("--------------------")
start_time = time.time()
for i in range(total_problems):
    
    expr,answer = generate_problem()
    try:
        user_answer = int(input(f"Problem #{i +1}: {expr} = "))
    except Exception as e:
        print(e)
        user_answer = ""
    if user_answer == answer:
        print("Your answer is correct!")
        score += 1
    else:
        print("Your answer is wrong!")
        print(f"The correct answer is: {answer}")
        wrong_answers.append((i, expr))

if  wrong_answers:
    print(f"You got {total_problems - score} answer wrong!")
    print("You have to attend them again!")
    print("------------------------------")
    a = input("press enter to attend the wrong answers or q to quit: ")
    if a == "":
        for wrong in wrong_answers:
            answer = int(input(f"Problem #{wrong[0] + 1}: {wrong[1]} = "))
            # print(eval(wrong[1]))
            # print(answer == int(eval(wrong[1])))
            if answer == int(eval(wrong[1])):
                score += 1
    
end_time = time.time()
total_time = round(end_time - start_time,2)
print(f"You finished this challenge in {total_time} seconds")
print(f"Your score is: {score}/{total_problems}")
if score == total_problems:
    print("Nice work!")
else:
    print("Keep practicing")
    

