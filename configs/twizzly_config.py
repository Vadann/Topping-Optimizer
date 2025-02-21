from models.cookie_config import CookieConfig

TWIZZLY_CONFIG = CookieConfig(
    name="Twizzly",
    base_stats={
        'Cooldown': 6,
        'DMG_Resist': 36.8,
        'ATK_SPD': 8.2,
        'Crit': 0,
    },
    required_stats={
        'Cooldown': 13.5,      # Exact CD
        'DMG_Resist': 65,      # Minimum DMR
    },
    topping_strategy=[
        ('chocolate', 5),      # 5 Swift Chocolate
    ],
    relevant_stats=['Crit', 'ATK_SPD', 'DMG_Resist'],
    min_relevant_stats=2
) 