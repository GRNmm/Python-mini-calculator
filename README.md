#  Mini-Calculator

A beginner-friendly Python project that allows users to perform basic arithmetic operations interactively. This project is designed to practice Python fundamentals such as variables, conditions, input/output, and type conversion.

---

##  Features
- Perform addition, subtraction, multiplication, and division  
- Simple and clean input/output  
- Lightweight and beginner-friendly  
- Easy to extend with new operations  

---

### Requirements
- Python 3.x installed on your system  

---

#### ⚡ Installation
Clone the repository and navigate to the project folder:
```bash
git clone https://github.com/GRNmm/mini-calculator.git
cd mini-calculator

____________________________________________________________________________________________________________
* Usage *
Run the script directly with Python:

bash
python calculator.py

Example
Input:
  sql
Enter first number: 5
Enter second number: 3
Choose operation (+, -, *, /): +
Output:

makefile
Result: 8.0

💻 Code Example
python
# Mini-Calculator by GRNmm

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operation")

__________________________________________________________________________________________________

🎯 Learning Goals
User input handling

Type conversion (float())

Conditional statements (if/elif/else)

Arithmetic operators

** License **
MIT License

Copyright (c) 2025 GRNmm

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.











