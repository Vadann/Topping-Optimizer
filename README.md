# Cookie Run: Kingdom Topping Optimizer

A powerful tool designed to optimize topping combinations for Cookie Run: Kingdom, with a primary focus on Guild Battle team compositions. This optimizer helps you find the perfect topping combinations from your inventory to meet specific stat requirements for each cookie.

## 🍪 Features

- Optimizes toppings for multiple cookies with different requirements
- Supports all topping types (Swift Chocolate, Solid Almond, Searing Raspberry, Apple Jelly)
- Considers multiple stats simultaneously (ATK, CD, ASPD, DMG Resist, etc.)
- Filters combinations based on minimum stat requirements
- Ranks combinations by effectiveness
- Provides detailed breakdowns of each topping combination

## 📋 Supported Cookies

Currently optimizes toppings for:
- Black Sapphire (5 AJ)
- Ferret (5 SC)
- Rebel (3 AJ + 2 SC)
- Twizzly (5 SC)
- Pinecone (3 SC + 2 CA)
- Dark Choco (5 SA)
- Crème Brûlée (3 SR + 2 AJ)
- Candy Apple (3 SR + 2 SA)
- Mint Choco (5 SC)
- Mystic Flower (3 SR + 2 SA)
- Palm Cookie (5 SA)

## 🚀 Getting Started

1️⃣ Clone the repository
```bash
git clone https://github.com/your-repo/cookie-run-optimizer.git
cd cookie-run-optimizer
```

2️⃣ Add Your Toppings (Toppings should be formatted in a Python dictionary list)
```python
toppings = [
    {
        "type": "apple_jelly",  # Topping type
        "ATK": 2.4,             # ATK substats
        "ATK_SPD": 0.0,         # Attack Speed substats
        "Crit": 2.5,            # Crit substats
        "Cooldown": 0.0,        # Cooldown substats
        "DMG_Resist": 0.0       # Damage Resist substats
    },
    # Add more toppings...
]
```

3️⃣ Run the Optimizer
```bash
python -m optimizations.black # For Black Sapphire
python -m optimizations.ferret # For Ferret
python -m optimizations.rebel # For Rebel

python -m optimizations.<cookie_name> # For other cookies
```

## 📊 Understanding the Output

The optimizer will show:
1. Number of toppings processed
2. Time taken to compute
3. Total combinations checked
4. Top 5 valid combinations with:
   - Total stats achieved
   - Detailed breakdown of each topping's contribution
   - Whether the combination meets all requirements

Example output:
```bash
Preprocessing Toppings for Black Sapphire:
--------------------------------------------------
Starting with 121 total toppings
apple_jelly toppings kept: 41/121
Total toppings kept: 41/121

Search completed in 1.78 seconds
Total combinations checked: 749398
Valid combinations found: 21059

Top 5 Combinations:
================================================================================

1. 5AJ Combination
Crit: 58.3
ATK: 34.3
CD: 8.7
------------------------------------------------------------
Type           Crit    ATK     CD
------------------------------------------------------------
apple_jelly    2.5     2.8     1.7
apple_jelly    2.9     1.5     1.7
apple_jelly    2.7     0.0     1.9
apple_jelly    2.5     0.0     1.8
apple_jelly    2.7     0.0     1.6

2. 5AJ Combination
Crit: 58.0
ATK: 36.0
CD: 8.9
------------------------------------------------------------
Type           Crit    ATK     CD
------------------------------------------------------------
apple_jelly    2.5     2.8     1.7
apple_jelly    2.9     1.5     1.7
apple_jelly    2.2     1.7     2.0
apple_jelly    2.7     0.0     1.9
apple_jelly    2.7     0.0     1.6

3. 5AJ Combination
Crit: 58.0
ATK: 34.3
CD: 8.7
------------------------------------------------------------
Type           Crit    ATK     CD
------------------------------------------------------------
apple_jelly    2.5     2.8     1.7
apple_jelly    2.9     1.5     1.7
apple_jelly    2.7     0.0     1.9
apple_jelly    2.5     0.0     1.8
apple_jelly    2.4     0.0     1.6

4. 5AJ Combination
Crit: 58.0
ATK: 34.3
CD: 8.7
------------------------------------------------------------
Type           Crit    ATK     CD
------------------------------------------------------------
apple_jelly    2.5     2.8     1.7
apple_jelly    2.9     1.5     1.7
apple_jelly    2.7     0.0     1.9
apple_jelly    2.5     0.0     1.8
apple_jelly    2.4     0.0     1.6

5. 5AJ Combination
Crit: 58.0
ATK: 33.2
CD: 9.0
------------------------------------------------------------
Type           Crit    ATK     CD
------------------------------------------------------------
apple_jelly    2.9     1.5     1.7
apple_jelly    2.2     1.7     2.0
apple_jelly    2.7     0.0     1.9
apple_jelly    2.5     0.0     1.8
apple_jelly    2.7     0.0     1.6
```

## 🔧 Customizing Requirements
Each cookie's requirements can be customized in their respective config files under `configs/`. You can modify:
- Base stats
- Required minimum/maximum stats
- Relevant stats to consider
- Topping strategy
- Minimum relevant substats per topping

## 📝 Contributing
Feel free to contribute by:
- Adding new cookie configurations
- Improving the optimization algorithm
- Adding new features
- Suggesting improvements
