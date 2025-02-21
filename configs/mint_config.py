from models.cookie_config import CookieConfig

MINT_CONFIG = CookieConfig(
    name="Mint Choco",
    base_stats={
        'Cooldown': 31.3,  # 15 + 5 + 11.3
        'ATK_SPD': 0,
    },
    required_stats={
        'ATK_SPD': 11.5,  # Minimum ATK_SPD
    },
    topping_strategy=[
        ('chocolate', 5),  # 5 Swift Chocolate
    ],
    relevant_stats=['Cooldown', 'ATK_SPD'],
    min_relevant_stats=1
) 