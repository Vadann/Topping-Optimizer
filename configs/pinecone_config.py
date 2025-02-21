from models.cookie_config import CookieConfig

PINECONE_CONFIG = CookieConfig(
    name="Pinecone",
    base_stats={
        'ATK_SPD': 44.4,
        'Cooldown': 9,
    },
    required_stats={
        'ATK_SPD': (57.6, 57.7),  # ATK_SPD range
        'Cooldown': 15.4,         # Target CD
    },
    topping_strategy=[
        ('chocolate', 3),
        ('caramel', 2)
    ],
    relevant_stats=['ATK_SPD', 'Cooldown'],
    min_relevant_stats=1
) 