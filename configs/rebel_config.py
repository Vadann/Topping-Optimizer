from models.cookie_config import CookieConfig

REBEL_CONFIG = CookieConfig(
    name="Rebel",
    base_stats={
        'Cooldown': 25.9,
        'ATK_SPD': 0,
        'Crit': 27,
    },
    required_stats={
        'Cooldown': 35.1,    # Minimum CD
        'ATK_SPD': 12.0,     # Minimum ATK_SPD
    },
    topping_strategy=[
        ('apple_jelly', 3),
        ('chocolate', 2),
    ],
    relevant_stats=['ATK_SPD', 'Cooldown', 'Crit'],
    min_relevant_stats=2
) 