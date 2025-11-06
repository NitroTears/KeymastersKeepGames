from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class EpicBattleFantasy3ArchipelagoOptions:
    pass

class EpicBattleFantasy3Game(Game):
    name = "Epic Battle Fantasy 3"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = EpicBattleFantasy3ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Must play on DIFFICULTY or Higher",
                data={
                    "DIFFICULTY": (self.difficulties, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Cannot use any Limit Breaks",
                data=dict(),
            ),
        ]
    
    def game_objective_templates(self) -> List [GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Defeat BOSS",
                data={
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Find all treasure chests in LOCATION",
                data={
                    "LOCATION": (self.locations, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
        ]
    

    @staticmethod
    def locations() -> List[str]:
        return [
            "Town",
            "Vegetable Forest",
            "Rock Lake",
            "Glacier Valley",
            "Kitten Ruins",
            "Volcano Peak",
        ]
    
    @staticmethod
    def bosses() -> List[str]:
        return [
            "Jack",
            "Gaint Squid",
            "Ancient Guardian",
            "Pyrohydra",
            "Akron",
        ]


    @staticmethod
    def difficulties() -> List[str]:
        return [
            "Normal",
            "Hard",
            "Epic",
        ]