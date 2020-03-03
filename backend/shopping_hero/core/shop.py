import uuid
from datetime import time
from shopping_hero.models.shop import Shop


def list_shops():
    return [Shop(uuid.uuid4(), "Lidl", 51.2, 38.89, time(8, 0), time(19, 0))]
