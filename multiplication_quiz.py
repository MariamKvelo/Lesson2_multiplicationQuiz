
print("\nWelcome to the simple multiplication quiz!" "\nYou will be given 5 multiplication problems to solve." "\nGood luck!")

import random

num_problems = 5
score = 0
problem = 1

for i in range(num_problems):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2
    user_answer = int(input(f"\nProblem {problem}: What is {num1} * {num2}? \nYour answer is: "))

    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer}")
    problem += 1

if score <=2:
    print(f"\nYour score is {score} out of {num_problems}. Please, practice more and try again!")
else:
    print(f"\nYour score is {score} out of {num_problems}. Well done!")


