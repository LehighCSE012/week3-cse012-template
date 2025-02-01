import pytest
import adventure
import random
from unittest.mock import patch
from io import StringIO
import sys

# --- Test combat_encounter function ---
def test_combat_encounter_player_wins_treasure(monkeypatch, capsys):
    """Test combat_encounter where player wins and monster has treasure."""
    # Mock attacks to ensure player wins quickly and monster has treasure
    def mock_player_attack(monster_health):
        return 0 # Player always wins
    def mock_monster_attack(player_health):
        return player_health # Monster does no damage

    monkeypatch.setattr(adventure, 'player_attack', mock_player_attack)
    monkeypatch.setattr(adventure, 'monster_attack', mock_monster_attack)

    initial_player_health = 100
    initial_monster_health = 75
    has_treasure = True
    treasure_result = adventure.combat_encounter(initial_player_health, initial_monster_health, has_treasure)
    captured = capsys.readouterr()
    assert "You defeated the monster!" in captured.out
    assert treasure_result is True # Should return True because player won and monster had treasure
