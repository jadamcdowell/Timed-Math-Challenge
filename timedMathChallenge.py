import random

# define the list of operators
OPERATORS = ["+", "-", "*"]

# define the min and max values for the operands
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problem():
    # generate random operands within the specified range
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    # randomly select an operator from the list
    operator = random.choice(OPERATORS)

    # construct the expression as a string
    expression = str(left) + "" + operator + str(right)

    # return the expression as a string
    return expression
