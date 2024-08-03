import json

from Arcanoid.ball import Ball
from Arcanoid.brick import Brick
from Arcanoid.platform_desk import PlatformDesk

__all__ = ["Ball", "Brick", "PlatformDesk"]
MAPS_PATH = "./maps/"

def get_game_params() -> dict:
    """
    Считывает параметры игры из файла конфигурации и возвращает их.

    Returns:
        dict: словарь, где ключи - название параметра, а значение - значение параметра.
    """
    CONFIG_PATH = "./configs.json"
    with open(CONFIG_PATH, encoding="utf-8") as file:
        configs = json.load(file)
    
    configs["ball_speed"] = max(12 - min(configs.get("ball_speed", 2), 10), 2)
    configs["platform_size"] = configs.get("platform_size", 11)
    configs["platform_speed"] = configs.get("platform_speed", 1)
    configs["level"] = configs.get("level", 1)
    configs["min_game_width"] = configs.get("min_game_width", 150)
    configs["min_game_height"] = configs.get("min_game_height", 40)

    return configs