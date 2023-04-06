from enum import Enum

class GameStage(Enum):
    """定义游戏阶段的枚举类"""
    start_menu = 0
    playing = 1
    game_over_menu = 2