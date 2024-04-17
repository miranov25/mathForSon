import random
from fractions import Fraction

def parse_answer(user_answer):
    try:
        # Evaluate as a fraction to handle fractional inputs
        return Fraction(user_answer)
    except ValueError:
        return None

def generate_problem(max_base, max_fraction):
    operations = [
        ("+", lambda x, y: x + y),
        ("-", lambda x, y: x - y),
        ("*", lambda x, y: x * y),
        ("/", lambda x, y: Fraction(x, y) if y != 0 else 'undefined')
    ]

    op_symbol, operation = random.choice(operations)
    num1, num2 = random.randint(1, max_base), random.randint(1, max_base)
    if op_symbol == '/':  # Ensure non-zero denominator for division
        while num2 == 0:
            num2 = random.randint(1, max_base)

    # Use "nicer" fractions by limiting denominators
    num1, num2 = Fraction(num1, random.randint(1, max_fraction)), Fraction(num2, random.randint(1, max_fraction))

    # Formulate the problem and solution
    problem = f"{num1} {op_symbol} {num2}"
    answer = operation(num1, num2)

    return problem, answer

def main(num_problems, max_base, max_fraction):
    correct_answers = 0
    problems = [generate_problem(max_base, max_fraction) for _ in range(num_problems)]

    for i, (problem, answer) in enumerate(problems, 1):
        print(f"Problem {i}: What is {problem}?")
        user_answer = input("Your answer: ")
        parsed_answer = parse_answer(user_answer)

        if parsed_answer is None:
            print("Invalid input! Please enter a valid number or fraction.")
        elif parsed_answer == answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {answer}")

    print(f"You got {correct_answers} out of {num_problems} correct!")

if __name__ == "__main__":
    import sys
    try:
        num_problems = int(sys.argv[1])
        max_base = int(sys.argv[2])
        max_fraction = int(sys.argv[3])
    except (IndexError, ValueError):
        num_problems = 5  # Default number of problems
        max_base = 30     # Default max base number
        max_fraction = 10 # Default max denominator for fractions
    main(num_problems, max_base, max_fraction)
