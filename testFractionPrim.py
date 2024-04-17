import tkinter as tk
from tkinter import messagebox
import random
from fractions import Fraction

class MathTestApp:
    def __init__(self, master, num_problems=5, max_base=30, max_fraction=10):
        self.master = master
        master.title("Math Test")

        self.num_problems = num_problems
        self.max_base = max_base
        self.max_fraction = max_fraction
        self.problems = []
        self.current_problem = 0
        self.correct_answers = 0

        self.generate_problems()

        self.problem_label = tk.Label(master, text="", font=("Helvetica", 16))
        self.problem_label.pack(pady=20)

        self.answer_entry = tk.Entry(master, font=("Helvetica", 14))
        self.answer_entry.pack(pady=20)

        self.check_button = tk.Button(master, text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.update_problem()

    def generate_problems(self):
        operations = [
            ("+", lambda x, y: x + y),
            ("-", lambda x, y: x - y),
            ("*", lambda x, y: x * y),
            ("/", lambda x, y: Fraction(x, y) if y != 0 else 'undefined')
        ]

        for _ in range(self.num_problems):
            op_symbol, operation = random.choice(operations)
            num1, num2 = random.randint(1, self.max_base), random.randint(1, self.max_base)
            if op_symbol == '/':
                while num2 == 0:
                    num2 = random.randint(1, self.max_base)
            num1, num2 = Fraction(num1, random.randint(1, self.max_fraction)), Fraction(num2, random.randint(1, self.max_fraction))
            problem = f"{num1} {op_symbol} {num2}"
            answer = operation(num1, num2)
            self.problems.append((problem, answer))

    def update_problem(self):
        if self.current_problem < len(self.problems):
            problem, _ = self.problems[self.current_problem]
            self.problem_label.config(text=f"Problem {self.current_problem+1}: What is {problem}?")
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("End of Test", f"You got {self.correct_answers} out of {self.num_problems} correct!")
            self.master.quit()

    def check_answer(self):
        _, answer = self.problems[self.current_problem]
        user_answer = self.answer_entry.get()
        try:
            if Fraction(user_answer) == answer:
                self.correct_answers += 1
                self.result_label.config(text="Correct!", fg='green')
            else:
                self.result_label.config(text=f"Wrong! The correct answer is {answer}", fg='red')
        except ValueError:
            self.result_label.config(text="Invalid input! Please enter a valid number or fraction.", fg='red')

        self.current_problem += 1
        self.master.after(1500, self.update_problem)

def main():
    root = tk.Tk()
    app = MathTestApp(root, 10, 30, 10)
    root.mainloop()

if __name__ == "__main__":
    main()
