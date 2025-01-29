from NewtonMainScriptHW1 import derivative_of_f, newton_method
import numpy as np

# Define a sample function f(e) - Example 4
def f(e):
    return  sigma - E * (1 + alpha * e) * e  # Example 4 /"nonlinear buckling equation" function for demonstration
    
# Given result from wolfram: 2.5e-7

# Given constants
E = 2e11  # Young's modulus in Pa (example for very soft material)
alpha = 0.01  # Material constant
sigma = 50000  # Applied stress in Pa (example)

# Initial guess x0
e0 = 0

# Impliment Newton Method
e = newton_method(f, derivative_of_f, e0, tolerance=1e-6, max_iter=100)
print("e =", e)