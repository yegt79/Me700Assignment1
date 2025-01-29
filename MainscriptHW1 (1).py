import numpy as np


# --- Function Definitions ---

def sort_values(x, y):
    """
    Ensures that the larger value is assigned to b and the smaller to a.
    Returns the sorted values as (a, b).
    """
    x = float(x)  # Convert x to a float
    y = float(y)  # Convert y to a float

    if x > y:
        sorted_x = y
        sorted_y = x
    else:
        sorted_x = x
        sorted_y = y
    return sorted_x, sorted_y


def calculate_mean(x, y):
    """
    Calculates the mean value of a and b.
    Returns the mean value.
    """
    return (x + y) / 2


def check_sign(x, y):
    """
    Checks if x and y have the same sign.
    Returns 1 if they have the same sign, 0 otherwise.
    """
    return 1 if np.sign(x) == np.sign(y) else 0


def reassign_ab(flag, a, b, c):
    """
    Reassigns a or b to c based on the flag value.
    If flag == 1, a = c. If flag == 0, b = c.
    Returns the new values of a and b.
    """
    if flag == 1:
        a = c
    else:
        b = c
    return a, b


# --- Test Definitions ---

def test_sort_values():
    # Test 1: Positive and negative numbers
    a = 10
    b = -5
    sorted_a, sorted_b = sort_values(a, b)
    try:
        assert np.isclose(sorted_a, -5)
        assert np.isclose(sorted_b, 10)
        print("test_sort_values - Test 1 Passed")
    except AssertionError:
        print("test_sort_values - Test 1 Failed")

    # Test 2: Both positive numbers
    a = 20
    b = 30
    sorted_a, sorted_b = sort_values(a, b)
    try:
        assert np.isclose(sorted_a, 20)
        assert np.isclose(sorted_b, 30)
        print("test_sort_values - Test 2 Passed")
    except AssertionError:
        print("test_sort_values - Test 2 Failed")

    # Test 3: Both negative numbers
    a = -10
    b = -20
    sorted_a, sorted_b = sort_values(a, b)
    try:
        assert np.isclose(sorted_a, -20)
        assert np.isclose(sorted_b, -10)
        print("test_sort_values - Test 3 Passed")
    except AssertionError:
        print("test_sort_values - Test 3 Failed")

    # Test 4: Zero and positive number
    a = 0
    b = 5
    sorted_a, sorted_b = sort_values(a, b)
    try:
        assert np.isclose(sorted_a, 0)
        assert np.isclose(sorted_b, 5)
        print("test_sort_values - Test 4 Passed")
    except AssertionError:
        print("test_sort_values - Test 4 Failed")

    # Test 5: Zero and negative number
    a = 0
    b = -5
    sorted_a, sorted_b = sort_values(a, b)
    try:
        assert np.isclose(sorted_a, -5)
        assert np.isclose(sorted_b, 0)
        print("test_sort_values - Test 5 Passed")
    except AssertionError:
        print("test_sort_values - Test 5 Failed")


def test_calculate_mean():
    # Test 1: Positive values
    a = 10
    b = 20
    mean = calculate_mean(a, b)
    try:
        assert np.isclose(mean, 15)
        print("test_calculate_mean - Test 1 Passed")
    except AssertionError:
        print("test_calculate_mean - Test 1 Failed")

    # Test 2: Negative values
    a = -10
    b = -20
    mean = calculate_mean(a, b)
    try:
        assert np.isclose(mean, -15)
        print("test_calculate_mean - Test 2 Passed")
    except AssertionError:
        print("test_calculate_mean - Test 2 Failed")

    # Test 3: Zero and positive value
    a = 0
    b = 10
    mean = calculate_mean(a, b)
    try:
        assert np.isclose(mean, 5)
        print("test_calculate_mean - Test 3 Passed")
    except AssertionError:
        print("test_calculate_mean - Test 3 Failed")

    # Test 4: Zero and negative value
    a = 0
    b = -10
    mean = calculate_mean(a, b)
    try:
        assert np.isclose(mean, -5)
        print("test_calculate_mean - Test 4 Passed")
    except AssertionError:
        print("test_calculate_mean - Test 4 Failed")

    # Test 5: Equal values
    a = 5
    b = 5
    mean = calculate_mean(a, b)
    try:
        assert np.isclose(mean, 5)
        print("test_calculate_mean - Test 5 Passed")
    except AssertionError:
        print("test_calculate_mean - Test 5 Failed")


def test_check_sign():
    # Test 1: Same sign, both positive
    x = 10
    y = 20
    flag = check_sign(x, y)
    try:
        assert np.isclose(flag, 1)
        print("test_check_sign - Test 1 Passed")
    except AssertionError:
        print("test_check_sign - Test 1 Failed")

    # Test 2: Different sign
    x = -10
    y = 20
    flag = check_sign(x, y)
    try:
        assert np.isclose(flag, 0)
        print("test_check_sign - Test 2 Passed")
    except AssertionError:
        print("test_check_sign - Test 2 Failed")

    # Test 3: Both negative
    x = -5
    y = -10
    flag = check_sign(x, y)
    try:
        assert np.isclose(flag, 1)
        print("test_check_sign - Test 3 Passed")
    except AssertionError:
        print("test_check_sign - Test 3 Failed")

    # Test 4: One positive and one negative
    x = -10
    y = 5
    flag = check_sign(x, y)
    try:
        assert np.isclose(flag, 0)
        print("test_check_sign - Test 4 Passed")
    except AssertionError:
        print("test_check_sign - Test 4 Failed")

    # Test 5: Both zero
    x = 0
    y = 0
    flag = check_sign(x, y)
    try:
        assert np.isclose(flag, 1)
        print("test_check_sign - Test 5 Passed")
    except AssertionError:
        print("test_check_sign - Test 5 Failed")


def test_reassign_ab():
    # Test 1: Flag = 1 (assign c to a)
    flag = 1
    a = 10
    b = 5
    c = 7
    new_a, new_b = reassign_ab(flag, a, b, c)
    try:
        assert np.isclose(new_a, 7)
        assert np.isclose(new_b, 5)
        print("test_reassign_ab - Test 1 Passed")
    except AssertionError:
        print("test_reassign_ab - Test 1 Failed")

    # Test 2: Flag = 0 (assign c to b)
    flag = 0
    a = 10
    b = 5
    c = 7
    new_a, new_b = reassign_ab(flag, a, b, c)
    try:
        assert np.isclose(new_a, 10)
        assert np.isclose(new_b, 7)
        print("test_reassign_ab - Test 2 Passed")
    except AssertionError:
        print("test_reassign_ab - Test 2 Failed")

    # Test 3: Assign a to c when flag is 1
    flag = 1
    a = 3
    b = 6
    c = 9
    new_a, new_b = reassign_ab(flag, a, b, c)
    try:
        assert np.isclose(new_a, 9)
        assert np.isclose(new_b, 6)
        print("test_reassign_ab - Test 3 Passed")
    except AssertionError:
        print("test_reassign_ab - Test 3 Failed")

    # Test 4: Assign b to c when flag is 0
    flag = 0
    a = 5
    b = 8
    c = 10
    new_a, new_b = reassign_ab(flag, a, b, c)
    try:
        assert np.isclose(new_a, 5)
        assert np.isclose(new_b, 10)
        print("test_reassign_ab - Test 4 Passed")
    except AssertionError:
        print("test_reassign_ab - Test 4 Failed")

    # Test 5: Test with zero
    flag = 1
    a = 0
    b = 8
    c = 10
    new_a, new_b = reassign_ab(flag, a, b, c)
    try:
        assert np.isclose(new_a, 10)
        assert np.isclose(new_b, 8)
        print("test_reassign_ab - Test 5 Passed")
    except AssertionError:
        print("test_reassign_ab - Test 5 Failed")


# --- Main Script ---

def run_all_tests():
    test_sort_values()
    test_calculate_mean()
    test_check_sign()
    test_reassign_ab()


if __name__ == "__main__":
     run_all_tests()
