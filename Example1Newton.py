from NewtonMainScriptHW1 import derivative_of_f, newton_method
import numpy as np

# Define a sample function f(x) - Example 1
def f(x):
    return x - 4  # Example 1 function for demonstration: f(x) = x-4

# Initial guess x0
x0 = 3

# Impliment Newton Method
x = newton_method(f, derivative_of_f, x0, tolerance=1e-6, max_iter=100)
print("x =", x)