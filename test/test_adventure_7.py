import pytest
import adventure
import random
from unittest.mock import patch
from io import StringIO
import sys


def test_monster_attack_critical_hit(monkeypatch, capsys):
    """Test monster_attack function with a critical hit."""
    monkeypatch.setattr(random, 'random', lambda: 0.4) # Mock random.random to return < 0.5 (critical hit)
    initial_player_health = 50
    updated_player_health = adventure.monster_attack(initial_player_health)
    captured = capsys.readouterr()
    assert "The monster lands a critical hit for 20 damage!" in captured.out
    assert updated_player_health == 30 # Player health reduced by 20
