from models.cookie_config import CookieConfig

PALM_CONFIG = CookieConfig(
    name="Palm",
    base_stats={
        'DMG_Resist': 40,
        'HP': 0,
        'ATK_SPD': 0,
    },
    required_stats={
        'DMG_Resist': 67.5,  # Minimum DMG_Resist
        'ATK_SPD': 11.3,     # Minimum ATK_SPD
    },
    topping_strategy=[
        ('almond', 5)  # 5 Solid Almond
    ],
    relevant_stats=['DMG_Resist', 'HP', 'ATK_SPD'],
    min_relevant_stats=2
) 