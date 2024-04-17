# MathForSon

A collection of Python scripts designed to help children practice basic math operations through both command line and graphical user interfaces. These tools focus on operations involving fractions, integers, and simplification of expressions to enhance arithmetic skills.

## Files

- `testFraction.py` - Command line interface version that generates math problems based on specified parameters.
- `testFractionPrim.py` - Graphical user interface version using Tkinter, providing a more interactive experience for solving math problems.

## Installation

Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/). These scripts were written using Python 3.8 or higher.

## Usage

### Command Line Version

Run `testFraction.py` from your command line by navigating to the directory containing the script and executing:

```bash
python testFraction.py [number_of_problems] [max_base] [max_fraction]
```

- `number_of_problems`: (Optional) The number of math problems to generate. Default is 5.
- `max_base`: (Optional) The maximum value for the base numbers used in problems. Default is 30.
- `max_fraction`: (Optional) The maximum value for the denominators used in problems. Default is 10.

### Graphical User Interface Version

Run `testFractionPrim.py` by navigating to the directory containing the script and executing:

```bash
python testFractionPrim.py
```

This will open a new window where math problems will be presented one at a time. Enter your answers directly into the interface.

## Features

- Generate a specified number of math problems involving fractions and integers.
- Choose from a range of difficulty levels by adjusting the max values for base numbers and fractions.
- Immediate feedback on answers through the GUI version with visual indications of correct or incorrect responses.

## Contributions

Contributions are welcome. If you have suggestions for improvements or have found bugs, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
