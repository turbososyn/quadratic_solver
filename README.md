# Quadratic Solver

A simple command-line tool to solve quadratic equations in ukrainian of the form:

```
ax² + bx + c = 0
```

---

## 🚀 Features

- Supports both interactive and non-interactive modes
- Handles real and complex roots
- Reads coefficients from user input or file
- Outputs results in a clear format

---

## ⚙️ How to Build & Run

### 1. Clone the Repository

```bash
git clone https://github.com/turbososyn/quadratic_solver.git
cd quadratic_solver
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Run (Interactive Mode)

```bash
python main.py
```

You will be prompted to enter the coefficients `a`, `b`, and `c`.

### 4. Run (Non-Interactive Mode)

```bash
python main.py input.txt
```

The `input.txt` file should contain coefficients in the following format:

```
1 2 1
2 5 -3
```

Each line represents a separate quadratic equation.

---

## 📄 Input File Format

- Each line must have three numbers separated by spaces: `a b c`
- Empty lines and lines with invalid input will be ignored

---

## 🔁 Revert Commit

Reverted commit: [`4df0df3`](https://github.com/turbososyn/quadratic_solver/commit/a65a03226ccd26235231d9676094495a60a83839)  

Reason: added some useless text

