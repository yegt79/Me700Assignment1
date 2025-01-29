from MainscriptHW1 import sort_values, calculate_mean, check_sign, reassign_ab
import numpy as np

# Define a sample function f1(x) - Example 1
def f1(e):
    return  sigma - E * (1 + alpha * e) * e # Example 4/ "nonlinear buckling equation" function for demonstration

# Given result from wolfram: 2.5e-7

# Given constants
E = 2e11  # Young's modulus in Pa (example for very soft material)
alpha = 0.01  # Material constant
sigma = 50000  # Applied stress in Pa (example)

# Initialize a and b
a = 7  # Example starting value
b = 0  # Example starting value

# Ensure a and b are sorted
a, b = sort_values(a, b)

# Initialize threshold
threshold = 0.01
fc = None  # Placeholder for f(c)

iteration = 0  # Initialize the iteration counter

while True:
    # Calculate mean (midpoint)
    iteration += 1  # Increment the iteration counter
    
    # Your loop code here
    
    if iteration > 200:
        print("Breaking the loop after 200 iterations")
        break  # Exit the loop if more than 200 iterations have been reached

    c = calculate_mean(a, b)
    
    # Evaluate f(a), f(b), and f(c)
    fa = f1(a)
    fb = f1(b)
    fc = f1(c)
    
    print(f"a = {a}, b = {b}, c = {c}, f(a) = {fa}, f(b) = {fb}, f(c) = {fc}")
    
    # Check if the result is within the threshold
    if abs(fc) < threshold:
        print(f"Root found at c = {c} with f(c) = {fc}")
        break
    
    # Check the sign of f(c) and f(a)
    flag = check_sign(fc, fa)
    
    # Reassign a and b based on the flag
    a, b = reassign_ab(flag, a, b, c)