import pytest
from main import vowel_count
from examples import EXAMPLES

@pytest.mark.parametrize('test_input, expected', EXAMPLES)
def test_vowel_count(test_input,expected):
    assert vowel_count(test_input) == expected
