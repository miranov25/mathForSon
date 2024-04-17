import random
from fractions import Fraction

def parse_answer(user_answer):
    try:
        # Try to evaluate as a float (for decimal inputs)
        return Fraction(user_answer)
    except ValueError:
        return None

def generate_problems(num_problems):
    operations = [
        ("+", lambda x, y: x + y),
        ("-", lambda x, y: x - y),
        ("*", lambda x, y: x * y),
        ("/", lambda x, y: Fraction(x, y) if y != 0 else 'undefined')
    ]

    problems = []
    for _ in range(num_problems):
        op_symbol, operation = random.choice(operations)
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        if op_symbol == '/':  # Ensure non-zero denominator for division
            while num2 == 0:
                num2 = random.randint(1, 10)

        # Formulate the problem and solution
        problem = f"{num1} {op_symbol} {num2}"
        answer = operation(num1, num2)
        problems.append((problem, answer))

    return problems

def main(num_problems):
    problems = generate_problems(num_problems)
    correct_answers = 0

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
    except (IndexError, ValueError):
        num_problems = 5  # default number of problems
    main(num_problems)
