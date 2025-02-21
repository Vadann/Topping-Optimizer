from models.cookie_config import CookieConfig

MYSTIC_CONFIG = CookieConfig(
    name="Mystic Guest",
    base_stats={
        'ATK': 60,
        'ATK_SPD': 0,
        'DMG_Resist': 0,
    },
    required_stats={
        'ATK': 75,  # Minimum ATK
        'ATK_SPD': 11.3,  # Minimum ATK_SPD
        'DMG_Resist': 30,  # Minimum DMG_Resist
    },
    topping_strategy=[
        ('raspberry', 3),
        ('almond', 2)
    ],
    relevant_stats=['ATK', 'ATK_SPD', 'DMG_Resist'],
    min_relevant_stats=2
) 