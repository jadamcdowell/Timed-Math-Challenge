import random
import time


# define the list of operators
OPERATORS = ["+", "-", "*"]

# define the min and max values for the operands
MIN_OPERAND = 3
MAX_OPERAND = 12

# define total problems
TOTAL_PROBLEMS = 10


def generate_problem():
    # generate random operands within the specified range
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    # randomly select an operator from the list
    operator = random.choice(OPERATORS)

    # construct the expression as a string
    exp = str(left) + "" + operator + str(right)

    ans = eval(exp)

    # return the expression and answer as a string
    return exp, ans


wrong = 0
correct = 0

input("Press enter to start challenge")
print("----------------------------")

start_time = time.time()

# loop to generate and solve random problems
for i in range(TOTAL_PROBLEMS):
    # generate math problem
    expression, answer = generate_problem()
    # loop until correct answer is provided
    while True:
        # prompt user with questions
        guess = input("Problem #" + str(i + 1) + ": " + expression + " = ")
        # check if the guess matches answer
        if guess == str(answer):
            correct += 1
            break
        else:
            wrong += 1
            break
# get the current time to calculate the end time of the program
end_time = time.time()

# calculate the total time by subtracting the start time from end time and rounding the result 2 places
total_time = round(end_time - start_time, 2)

# display the results
print("\n---------Results----------")
print("Correct: " + str(correct) + "\tIncorrect: " + str(wrong))
print("Nice work! You finished in " + str(total_time) + " seconds.")
