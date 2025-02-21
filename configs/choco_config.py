from models.cookie_config import CookieConfig

CHOCO_CONFIG = CookieConfig(
    name="Choco",
    base_stats={
        'Cooldown': 7.9,
        'HP': 0,
        'DMG_Resist': 0,
    },
    required_stats={
        'Cooldown': 7.9,  # Exact CD
    },
    topping_strategy=[
        ('almond', 5),  # 5 Solid Almond
    ],
    relevant_stats=['Cooldown', 'HP', 'DMG_Resist'],
    min_relevant_stats=2
) 