import pytest
import adventure
import random
from unittest.mock import patch
from io import StringIO
import sys

# --- Test display_player_status function ---
def test_display_player_status(capsys):
    """Test display_player_status function."""
    health = 70
    adventure.display_player_status(health)
    captured = capsys.readouterr()
    assert f"Your current health: {health}" in captured.out