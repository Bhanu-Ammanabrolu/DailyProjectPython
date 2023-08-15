import random
import time

OPERATORS = ["+", "-", "*"]

MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEM = 10


def problem_generator():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)
    return expression, answer


wrong = 0
input("Press ENTER to start the Timer.")
print("--------*********-----------")

start_time = time.time()

for i in range(TOTAL_PROBLEM):
    expr, result = problem_generator()
    while True:
        guess = int(input(f"question<{i+1} is - {expr} = "))
        if guess == result:
            break
        else:
            wrong += 1
            print("Try again....")

end_time = time.time()
total_time = end_time - start_time

print(f"No of times wrong - {wrong}")
print(f"Nice work done! --- finished in {round(total_time, 2)} seconds!")
