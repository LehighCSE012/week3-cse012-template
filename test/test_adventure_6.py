import pytest
import adventure
import random
from unittest.mock import patch
from io import StringIO
import sys


# --- Test monster_attack function ---
def test_monster_attack_normal_hit(monkeypatch, capsys):
    """Test monster_attack function with a normal hit."""
    monkeypatch.setattr(random, 'random', lambda: 0.6) # Mock random.random to return >= 0.5 (normal hit)
    initial_player_health = 50
    updated_player_health = adventure.monster_attack(initial_player_health)
    captured = capsys.readouterr()
    assert "The monster hits you for 10 damage!" in captured.out
    assert updated_player_health == 40 # Player health reduced by 10