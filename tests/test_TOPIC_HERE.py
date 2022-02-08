
import numpy as np

from template_repo.module_A.example_code import add_numbers


def test_FUNCTION_NAME():
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
