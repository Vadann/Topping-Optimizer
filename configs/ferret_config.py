from models.cookie_config import CookieConfig

FERRET_CONFIG = CookieConfig(
    name="Ferret",
    base_stats={
        'Cooldown': 30.4,
        'ATK_SPD': 0,
    },
    required_stats={
        'Cooldown': 40.3,  # Target CD
        'ATK_SPD': 9.2,    # Minimum ATK_SPD
    },
    topping_strategy=[
        ('chocolate', 5),  # 5 Swift Chocolate
    ],
    relevant_stats=['Cooldown', 'ATK_SPD'],
    min_relevant_stats=1
) 