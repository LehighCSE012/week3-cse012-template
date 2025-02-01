import pytest
import adventure
import random
from unittest.mock import patch
from io import StringIO
import sys


# --- Test check_for_treasure function ---
@pytest.mark.parametrize("has_treasure_input, expected_output", [
    (True, "You found the hidden treasure! You win!"),
    (False, "The monster did not have the treasure. You continue your journey.")
])
def test_check_for_treasure(capsys, has_treasure_input, expected_output):
    """Test check_for_treasure function for both treasure and no treasure cases."""
    adventure.check_for_treasure(has_treasure_input)
    captured = capsys.readouterr()
    assert expected_output in captured.out
