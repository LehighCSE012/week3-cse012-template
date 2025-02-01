import pytest
import adventure
import random
from unittest.mock import patch
from io import StringIO
import sys

# --- Test handle_path_choice function ---
def test_handle_path_choice_left(monkeypatch, capsys):
    """Test handle_path_choice with 'left' path."""
    monkeypatch.setattr(random, 'choice', lambda _: 'left') # Mock random.choice to always return 'left'
    initial_health = 50
    updated_health = adventure.handle_path_choice(initial_health)
    captured = capsys.readouterr()
    assert "You encounter a friendly gnome" in captured.out
    assert updated_health == 60 # Health increased by 10
    assert updated_health <= 100 # Health does not exceed 100

def test_handle_path_choice_right(monkeypatch, capsys):
    """Test handle_path_choice with 'right' path."""
    monkeypatch.setattr(random, 'choice', lambda _: 'right') # Mock random.choice to always return 'right'
    initial_health = 50
    updated_health = adventure.handle_path_choice(initial_health)
    captured = capsys.readouterr()
    assert "You fall into a pit" in captured.out
    assert updated_health == 35 # Health decreased by 15

def test_handle_path_choice_right_barely_alive(monkeypatch, capsys):
    """Test handle_path_choice 'right' path with health dropping to 0."""
    monkeypatch.setattr(random, 'choice', lambda _: 'right') # Mock random.choice to always return 'right'
    initial_health = 10
    updated_health = adventure.handle_path_choice(initial_health)
    captured = capsys.readouterr()
    assert "You fall into a pit" in captured.out
    assert "You are barely alive!" in captured.out
    assert updated_health == 0 # Health becomes 0

# --- Test player_attack function ---
def test_player_attack(capsys):
    """Test player_attack function."""
    initial_monster_health = 75
    updated_monster_health = adventure.player_attack(initial_monster_health)
    captured = capsys.readouterr()
    assert "You strike the monster for 15 damage!" in captured.out
    assert updated_monster_health == 60 # Monster health reduced by 15
