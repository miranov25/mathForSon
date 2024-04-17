import random
from fractions import Fraction

def parse_answer(user_answer):
    try:
        # Try to evaluate as a float (for decimal inputs)
        return float(user_answer)
    except ValueError:
        try:
            # If float conversion fails, try to evaluate as a fraction
            return float(Fraction(user_answer))
        except ValueError:
            # If both conversions fail, return None to indicate an error
            return None

def generate_problems(num_problems):
    operations = [
        ("+", lambda x, y: x + y),
        ("-", lambda x, y: x - y),
        ("*", lambda x, y: x * y),
        ("/", lambda x, y: x / y)
    ]
    
    problems = []
    for _ in range(num_problems):
        op_symbol, operation = random.choice(operations)
        if random.choice([True, False]):
            # Generate fraction problems
            numer1, denom1 = random.randint(1, 10), random.randint(1, 10)
            numer2, denom2 = random.randint(1, 10), random.randint(1, 10)
            num1, num2 = Fraction(numer1, denom1), Fraction(numer2, denom2)
        else:
            # Generate decimal/integer problems
            num1, num2 = random.randint(1, 10), random.randint(1, 10)
            if random.choice([True, False]):
                num1 /= random.randint(1, 10)
                num2 /= random.randint(1, 10)
        
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
        elif parsed_answer == float(answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {answer}")

    print(f"You got {correct_answers} out of {num_problems} correct!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        num_problems = int(sys.argv[1])
    else:
        num_problems = 5  # default number of problems
    main(num_problems)
