from models.cookie_config import CookieConfig

BLACK_CONFIG = CookieConfig(
    name="Black Sapphire",
    base_stats={
        'Crit': 45.0,
        'ATK': 30.0,
        'Cooldown': 0,
    },
    required_stats={
        'Cooldown': 8.7,  # Minimum CD
    },
    topping_strategy=[
        ('apple_jelly', 5),  # 5 Apple Jelly
    ],
    relevant_stats=['Cooldown', 'Crit', 'ATK'],
    min_relevant_stats=2
) 