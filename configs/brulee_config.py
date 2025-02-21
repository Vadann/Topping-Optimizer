from models.cookie_config import CookieConfig

BRULEE_CONFIG = CookieConfig(
    name="Crème Brûlée",
    base_stats={
        'ATK': 60,
        'Crit': 13,
        'ATK_SPD': 0,
    },
    required_stats={
        'ATK': 75,  # Minimum ATK
        'ATK_SPD': (11.5, 12.5),  # ATK_SPD range
    },
    topping_strategy=[
        ('raspberry', 3),
        ('apple_jelly', 2)
    ],
    relevant_stats=['ATK', 'Crit', 'ATK_SPD'],
    min_relevant_stats=2
) 