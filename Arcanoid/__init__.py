import json

GAME_SIZE_X = 150
GAME_SIZE_Y = 40
CONFIG_PATH = "./configs.json"
MAPS_PATH = "./maps/"

with open(CONFIG_PATH) as file:
    configs = json.load(file)

BALL_SPEED = 12 - min(configs.get("ball_speed", 10), 10)
PLATFORM_SIZE = configs.get("platform_size", 11)
PLATFORM_SPEED = configs.get("platform_speed", 1)
LEVEL = configs.get("level", 1)
