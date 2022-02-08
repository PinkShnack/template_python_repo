
import numpy as np

from template_repo.module_A.example_code import add_numbers, add_numbers_numpy


def test_add_numbers():
    """Descriptive docstring"""
    # arrange
    a = 5
    b = 3
    expected_result = 8

    # act
    actual_result = add_numbers(a=a, b=b)

    # assert
    assert actual_result == expected_result
    # or if they are arrays
    assert np.allclose(actual_result, expected_result)


def test_compare_add_numbers_numpy():
    """Descriptive docstring"""
    # arrange
    a = 5
    b = 3
    expected_result = 8

    # act
    actual_result = add_numbers(a=a, b=b)
    actual_result_numpy = add_numbers_numpy(a=a, b=b)

    # assert
    assert actual_result_numpy == expected_result
    assert actual_result_numpy == actual_result
    # or if they are arrays
    assert np.allclose(actual_result_numpy, expected_result)
    assert np.allclose(actual_result, expected_result)
