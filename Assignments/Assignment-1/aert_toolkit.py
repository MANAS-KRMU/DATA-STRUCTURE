# Algorithmic Efficiency & Recursion Toolkit
# Name: ______________________
# Roll No: ____________________




# -------------------------------
# PART B: Factorial (Recursive)
# -------------------------------

def factorial(n):
    if n < 0:
        return "Invalid input (n must be >= 0)"
    if n == 0:
        return 1
    return n * factorial(n - 1)