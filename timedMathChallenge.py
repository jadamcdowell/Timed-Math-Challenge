import random

# define the list of operators
OPERATORS = ["+", "-", "*"]

# define the min and max values for the operands
MIN_OPERAND = 3
MAX_OPERAND = 12

# define total problems
TOTAL_PROBLEMS = 5

def generate_problem():
    # generate random operands within the specified range
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    # randomly select an operator from the list
    operator = random.choice(OPERATORS)

    # construct the expression as a string
    expression = str(left) + "" + operator + str(right)

    answer = eval(expression)

    # return the expression and answer as a string
    return expression, answer

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
            break
