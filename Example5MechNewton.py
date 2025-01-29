from NewtonMainScriptHW1 import derivative_of_f, newton_method
import numpy as np

# Define a sample function f(v) - Example 5
def f(v):
    return  C - P * v**n # Example 5/ "Nonlinear Pressure-Volume Relationship (Polytropic Process)" function for demonstration
    
# Given result from wolfram: 2.6918

# Given constants
P = 50000    # Given pressure (Pa)
C = 200000   # Constant from the polytropic equation
n = 1.4      # Polytropic index

# Initial guess x0
v0 = 1

# Impliment Newton Method
v = newton_method(f, derivative_of_f, v0, tolerance=1e-6, max_iter=100)
print("v =", v)