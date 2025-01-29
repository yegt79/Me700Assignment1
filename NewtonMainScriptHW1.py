import numpy as np


def derivative_of_f(f, x):
    """
    Returns the numerical derivative of the function f at point x.
    Uses the finite difference method with step size h.
    """
    h = 1e-5
    return (f(x + h) - f(x)) / h



# Test function for numerical derivatives with 5 different tests
def test_derivative_of_f_numpy():
    """
    Test the numerical derivative function for different functions.
    """
    threshold = 0.001

    # Test 1: f(x) = x^2 - 4
    def f(x):
        return x**2 - 4
    x_value = 2
    f_prime = derivative_of_f(f, x_value)
    try:
        assert np.isclose(f_prime, 4, atol=threshold)  # The derivative at x = 2 is 4
        print("test_derivative_of_f_numpy - Test 1 Passed")
    except AssertionError:
        print(f"test_derivative_of_f_numpy - Test 1 Failed, f_prime: {f_prime}")

    # Test 2: f(x) = sin(x)
    def f(x):
        return np.sin(x)
    x_value = np.pi / 2
    f_prime = derivative_of_f(f, x_value)
    try:
        assert np.isclose(f_prime, 0, atol=threshold)  # The derivative of sin(x) at pi/2 is 0
        print("test_derivative_of_f_numpy - Test 2 Passed")
    except AssertionError:
        print(f"test_derivative_of_f_numpy - Test 2 Failed, f_prime: {f_prime}")

    # Test 3: f(x) = x^3
    def f(x):
        return x**3
    x_value = 1
    f_prime = derivative_of_f(f, x_value)
    try:
        assert np.isclose(f_prime, 3, atol=threshold)  # The derivative of x^3 at x = 1 is 3
        print("test_derivative_of_f_numpy - Test 3 Passed")
    except AssertionError:
        print(f"test_derivative_of_f_numpy - Test 3 Failed, f_prime: {f_prime}")

    # Test 4: f(x) = e^x
    def f(x):
        return np.exp(x)
    x_value = 0
    f_prime = derivative_of_f(f, x_value)
    try:
        assert np.isclose(f_prime, 1, atol=threshold)  # The derivative of e^x at x = 0 is 1
        print("test_derivative_of_f_numpy - Test 4 Passed")
    except AssertionError:
        print(f"test_derivative_of_f_numpy - Test 4 Failed, f_prime: {f_prime}")

    # Test 5: f(x) = cos(x)
    def f(x):
        return np.cos(x)
    x_value = np.pi
    f_prime = derivative_of_f(f, x_value)
    try:
        assert np.isclose(f_prime, 0, atol=threshold)  # The derivative of cos(x) at x = pi is 0
        print("test_derivative_of_f_numpy - Test 5 Passed")
    except AssertionError:
        print(f"test_derivative_of_f_numpy - Test 5 Failed, f_prime: {f_prime}")




def newton_method(f, derivative_of_f, x0, tolerance=1e-6, max_iter=100):
    """
    Applies Newton's method to find the root of the function f(x).
    
    Args:
    f: The function whose root is to be found.
    f_prime: The derivative of the function f(x).
    x0: Initial guess for the root.
    tolerance: Desired tolerance for stopping the method.
    max_iter: Maximum number of iterations allowed.
    
    Returns:
    The estimated root of the function.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = derivative_of_f(f, x)
        
        # Avoid division by zero
        if fpx == 0:
            print("Derivative is zero. No solution found.")
            return None
        
        # Newton's method formula
        x_new = x - fx / fpx
        
        # Check if the result is within the desired tolerance
        if abs(x_new - x) < tolerance:
            return x_new
        
        x = x_new
    
    print("Max iterations reached. Solution may not have converged.")
    return x


# --- Test Definitions for Newton's Method ---
def test_newton_method():
    """
    Test for Newton's method on the function f(x) = x^2 - 4.
    The root should be x = 2.
    """
    
    # Define the function and its derivative
    def f(x):
        return x**2 - 4
    
    def derivative_of_f(f, x):
        return 2*x
    
    # Initial guess
    x0 = 3.0
    
    # Apply Newton's method
    root = newton_method(f, derivative_of_f, x0)
    
    # Test if the result is correct (root = 2)
    try:
        assert np.isclose(root, 2)
        print("test_newton_method - Passed")
    except AssertionError:
        print("test_newton_method - Failed")


# --- Main Script ---

def run_all_tests():
    test_newton_method()
    test_derivative_of_f_numpy()


if __name__ == "__main__":
    run_all_tests()
