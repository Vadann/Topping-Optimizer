from itertools import combinations
import random
import time



# Load toppings from your toppings.txt file
# ... (toppings data loading) ...

toppings = [
    {'type': 'raspberry', 'ATK': 2.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.9},
    {'type': 'raspberry', 'ATK': 2.5, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.7},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 1.2, 'ATK_SPD': 2.2, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 1.1, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.5, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 3.0, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 2.2, 'Cooldown': 0.0, 'DMG_Resist': 2.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 1.9, 'DMG_Resist': 2.5},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 5.4},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.5, 'Crit': 2.4, 'Cooldown': 1.3, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.4, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.2, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.2, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.4, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.1, 'Cooldown': 1.2, 'DMG_Resist': 5.1},
    {'type': 'raspberry', 'ATK': 2.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 1.8, 'ATK_SPD': 1.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 1.3, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.2},
    {'type': 'raspberry', 'ATK': 3.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.8, 'ATK_SPD': 1.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.4},
    {'type': 'raspberry', 'ATK': 2.7, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.3},
    {'type': 'raspberry', 'ATK': 2.7, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.7},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 1.2, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.3, 'ATK_SPD': 0.0, 'Crit': 1.3, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.3, 'ATK_SPD': 0.0, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.3, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.3, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 1.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 5.9},
    {'type': 'raspberry', 'ATK': 2.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.3},
    {'type': 'raspberry', 'ATK': 1.9, 'ATK_SPD': 0.0, 'Crit': 1.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 1.2, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 1.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.7, 'ATK_SPD': 0.0, 'Crit': 2.5, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.3},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.5, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 1.3, 'ATK_SPD': 0.0, 'Crit': 1.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 3.0, 'Crit': 1.5, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 4.0},
    {'type': 'raspberry', 'ATK': 1.9, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 1.2, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 1.4, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 4.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.5},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.9},
    {'type': 'raspberry', 'ATK': 2.9, 'ATK_SPD': 2.3, 'Crit': 1.3, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.7, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 1.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 3.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 3.0, 'Cooldown': 0.0, 'DMG_Resist': 4.5},
    {'type': 'raspberry', 'ATK': 1.6, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 1.1, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 3.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 0.0, 'DMG_Resist': 2.2},
    {'type': 'raspberry', 'ATK': 1.5, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.3, 'Crit': 2.5, 'Cooldown': 1.2, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.3, 'Crit': 1.7, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 4.7},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 1.8, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.9, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.3, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.3, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.9, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 2.8},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.5, 'Cooldown': 1.7, 'DMG_Resist': 1.3},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.3, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.0, 'ATK_SPD': 1.7, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.5, 'Cooldown': 1.4, 'DMG_Resist': 5.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.7, 'Cooldown': 1.4, 'DMG_Resist': 3.7},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.9},
    {'type': 'raspberry', 'ATK': 2.7, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
    {'type': 'raspberry', 'ATK': 2.2, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.5},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 1.6, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.2, 'Cooldown': 0.0, 'DMG_Resist': 5.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.8},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.3, 'Cooldown': 0.0, 'DMG_Resist': 4.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 3.3},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 0.0, 'DMG_Resist': 3.2},
    {'type': 'raspberry', 'ATK': 2.6, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 3.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.8},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 2.5},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 1.4},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.6, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.1},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.8},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 1.0, 'Crit': 2.2, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 2.8, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 3.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 1.0},
    {'type': 'chocolate', 'ATK': 2.6, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.2, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.2, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.7},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 3.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 5.2},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.1, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.4, 'ATK_SPD': 2.7, 'Crit': 2.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 3.0, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.9, 'Cooldown': 0.0, 'DMG_Resist': 4.0},
    {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 1.2, 'Crit': 1.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 1.4},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.0, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 3.2},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.9, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 2.2},
    {'type': 'chocolate', 'ATK': 2.6, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 4.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 2.3},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 1.4, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 1.3, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 2.6},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 2.7, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
    {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 1.1, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.7, 'ATK_SPD': 3.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.6, 'ATK_SPD': 2.3, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
    {'type': 'chocolate', 'ATK': 2.6, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.6},
    {'type': 'chocolate', 'ATK': 2.5, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.5, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.5, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.1},
    {'type': 'chocolate', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.3, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.3, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.7},
    {'type': 'chocolate', 'ATK': 1.5, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 3.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.2, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 5.0},
    {'type': 'chocolate', 'ATK': 2.6, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.4},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 1.2, 'DMG_Resist': 3.1},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.7, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.3},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 3.0, 'Cooldown': 0.0, 'DMG_Resist': 2.1},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 3.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 4.9},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.1, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.6, 'ATK_SPD': 0.0, 'Crit': 2.9, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 2.7, 'Cooldown': 1.2, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.1, 'Crit': 2.6, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.7, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.1, 'ATK_SPD': 1.7, 'Crit': 2.5, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.6, 'ATK_SPD': 0.0, 'Crit': 2.4, 'Cooldown': 0.0, 'DMG_Resist': 3.1},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 2.3, 'Cooldown': 0.0, 'DMG_Resist': 4.8},
    {'type': 'chocolate', 'ATK': 1.9, 'ATK_SPD': 0.0, 'Crit': 2.2, 'Cooldown': 0.0, 'DMG_Resist': 3.3},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 9.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 4.7},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 2.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.1, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 3.5},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.6, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.3, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.3, 'Crit': 1.1, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 1.8, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.0, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.6, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 1.7, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.9, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.3, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 5.5},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.7, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.7, 'Cooldown': 1.6, 'DMG_Resist': 1.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.6, 'DMG_Resist': 5.7},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.2, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 1.5, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 2.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.8, 'Cooldown': 1.4, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.4, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.6, 'Cooldown': 1.3, 'DMG_Resist': 2.2},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.3, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.3, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.2, 'DMG_Resist': 5.5},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.2, 'DMG_Resist': 4.4},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 1.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.0, 'Cooldown': 0.0, 'DMG_Resist': 6.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.9},
    {'type': 'chocolate', 'ATK': 1.8, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 5.8},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.5, 'DMG_Resist': 5.8},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.7},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.4},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 5.4},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 5.3},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 5.3},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.2},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.1},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.7},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.8, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.7},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.9, 'DMG_Resist': 4.7},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.6},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.3, 'Cooldown': 0.0, 'DMG_Resist': 4.5},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.2, 'Crit': 0.0, 'Cooldown': 1.4, 'DMG_Resist': 4.5},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'chocolate', 'ATK': 1.6, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.4},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 1.4, 'Crit': 2.9, 'Cooldown': 0.0, 'DMG_Resist': 4.3},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.3},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.2},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.1},
    {'type': 'chocolate', 'ATK': 1.6, 'ATK_SPD': 2.2, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.1},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.0, 'DMG_Resist': 4.0},
    {'type': 'chocolate', 'ATK': 1.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 4.0},
    {'type': 'chocolate', 'ATK': 1.8, 'ATK_SPD': 2.5, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.9},
    {'type': 'chocolate', 'ATK': 1.2, 'ATK_SPD': 0.0, 'Crit': 1.3, 'Cooldown': 0.0, 'DMG_Resist': 3.7},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.9, 'Crit': 2.2, 'Cooldown': 0.0, 'DMG_Resist': 3.5},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.5},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.1, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.3},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 3.2},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.0, 'Cooldown': 0.0, 'DMG_Resist': 3.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 3.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.9},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.3},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 2.3},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.8, 'Cooldown': 0.0, 'DMG_Resist': 2.2},
    {'type': 'chocolate', 'ATK': 1.9, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.9},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.2, 'DMG_Resist': 1.3},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 1.2},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 1.1, 'DMG_Resist': 1.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.4, 'Crit': 1.9, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 1.8, 'Cooldown': 1.9, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 2.9, 'ATK_SPD': 1.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 1.1, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 2.6, 'Crit': 2.7, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.6, 'Cooldown': 0.0, 'DMG_Resist': 0.0},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 3.1},
    {'type': 'raspberry', 'ATK': 2.4, 'ATK_SPD': 0.0, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.1},
    {'type': 'chocolate', 'ATK': 2.4, 'ATK_SPD': 2.6, 'Crit': 0.0, 'Cooldown': 0.0, 'DMG_Resist': 5.1},
    {'type': 'chocolate', 'ATK': 0.0, 'ATK_SPD': 0.0, 'Crit': 2.8, 'Cooldown': 2.0, 'DMG_Resist': 5.8},
    {'type': 'raspberry', 'ATK': 0.0, 'ATK_SPD': 2.7, 'Crit': 0.0, 'Cooldown': 1.8, 'DMG_Resist': 5.4},
    
        

        ]
print("Starting code... ")

# Base values

base_atk = 60  # 30 + 27 + 3
base_cooldown = 11.7
base_dmg_resist = 0
# Input your current stats here (base + toppings)
current_atk = base_atk + 8.5  # Example - replace with your current value
current_cooldown = base_cooldown + 3.6  # Example - replace with your current value
current_dmg_resist = 27.9  # Example - replace with your current value
# Define requirement ranges
cooldown_range = (14.3, 20.0)  # At least 14.3
dmg_resist_range = (27, 30.0)  # Between 27-30

def create_initial_population(raspberry_toppings, chocolate_toppings, size=200):
    population = []
    for _ in range(size):
        rasp = random.sample(raspberry_toppings, 3)
        choc = random.sample(chocolate_toppings, 2)
        population.append(rasp + choc)
    return population

def evaluate_combo(combo):
    # Convert dictionaries to tuples for comparison
    combo_set = set(tuple(sorted(t.items())) for t in combo)
    if len(combo_set) != len(combo):
        return -1000
        
    total_atk = sum(t['ATK'] for t in combo) + base_atk
    total_cooldown = sum(t['Cooldown'] for t in combo) + base_cooldown
    total_dmg_resist = sum(t['DMG_Resist'] for t in combo)
    
    if cooldown_range[0] <= total_cooldown <= cooldown_range[1] and dmg_resist_range[0] <= total_dmg_resist <= dmg_resist_range[1]:
        return total_atk
    return -1000
def generate_valid_combo(raspberry_toppings, apple_jelly_toppings):
    # Use combinations to ensure unique toppings
    rasp = list(random.sample(raspberry_toppings, 3))
    apple = list(random.sample(apple_jelly_toppings, 2))
    return rasp + apple

def crossover(parent1, parent2):
    # Get raspberry and chocolate toppings from parents
    rasp1 = parent1[:3]
    rasp2 = parent2[:3]
    choc1 = parent1[3:]
    choc2 = parent2[3:]
    
    # Create pools of unique toppings
    rasp_pool = []
    for t in rasp1 + rasp2:
        if t not in rasp_pool:
            rasp_pool.append(t)
            
    choc_pool = []
    for t in choc1 + choc2:
        if t not in choc_pool:
            choc_pool.append(t)
    
    # Create child using available toppings
    if len(rasp_pool) >= 3 and len(choc_pool) >= 2:
        child_rasp = random.sample(rasp_pool, 3)
        child_choc = random.sample(choc_pool, 2)
        return child_rasp + child_choc
    else:
        return parent1

def mutate(combo, raspberry_toppings, chocolate_toppings, mutation_rate=0.3):
    if random.random() < mutation_rate:
        # Create lists of unused toppings
        used_toppings = combo.copy()
        if random.random() < 0.6:
            # Mutate raspberry
            available_rasp = [t for t in raspberry_toppings if t not in used_toppings]
            if available_rasp:
                idx = random.randint(0, 2)
                combo[idx] = random.choice(available_rasp)
        else:
            # Mutate chocolate
            available_choc = [t for t in chocolate_toppings if t not in used_toppings]
            if available_choc:
                idx = random.randint(3, 4)
                combo[idx] = random.choice(available_choc)
    return combo

def genetic_algorithm(toppings, generations=100, population_size=200):
    raspberry_toppings = [t for t in toppings if t['type'] == 'raspberry']
    chocolate_toppings = [t for t in toppings if t['type'] == 'chocolate']
    
    print(f"Checking {len(raspberry_toppings)} raspberry and {len(chocolate_toppings)} chocolate toppings...")
    
    population = create_initial_population(raspberry_toppings, chocolate_toppings, population_size)
    best_combo = None
    max_atk = float('-inf')
    
    for gen in range(generations):
        scored_population = [(combo, evaluate_combo(combo)) for combo in population]
        scored_population.sort(key=lambda x: x[1], reverse=True)
        
        current_best_score = scored_population[0][1]
        if current_best_score > max_atk and current_best_score != -1000:
            max_atk = current_best_score
            best_combo = scored_population[0][0]
        
        if gen % 10 == 0:
            print(f"Generation {gen}: Best ATK = {max_atk if max_atk > float('-inf') else 'None found'}")
        
        # Keep best valid combinations
        new_population = [combo for combo, score in scored_population[:20] if score > -1000]
        
        # Add random combinations if needed
        while len(new_population) < 20:
            new_combo = create_initial_population(raspberry_toppings, chocolate_toppings, 1)[0]
            new_population.append(new_combo)
        
        # Generate rest of new population
        while len(new_population) < population_size:
            parents = random.choices(new_population, k=2)
            child = crossover(parents[0], parents[1])
            child = mutate(child, raspberry_toppings, chocolate_toppings)
            new_population.append(child)
        
        population = new_population
    
    return best_combo, max_atk

# Start timing
start_time = time.time()

# Run genetic algorithm
best_combo, max_atk = genetic_algorithm(toppings)

# End timing
end_time = time.time()

# Output the result
# Output the result
if best_combo:
    total_atk = max_atk
    total_cooldown = sum(t['Cooldown'] for t in best_combo) + base_cooldown
    total_dmg_resist = sum(t['DMG_Resist'] for t in best_combo)

    print(f"\nTime taken: {end_time - start_time:.2f} seconds")
    
    # Current stats (before)
    print("\nCurrent Stats:")
    print("-" * 50)
    print(f"{'Current ATK:':<20}{current_atk:.2f}")
    print(f"{'Current Cooldown:':<20}{current_cooldown:.2f}")
    print(f"{'Current DMG_Resist:':<20}{current_dmg_resist:.2f}")
    print("-" * 50)
    
    # Best combo found
    print("\nBest combo found:")
    print("-" * 50)
    print(f"{'Topping Type':<15}{'ATK':<10}{'Cooldown':<10}{'DMG_Resist':<10}")
    print("-" * 50)
    for topping in best_combo:
        print(f"{topping['type']:<15}{topping['ATK']:<10.1f}{topping['Cooldown']:<10.1f}"
              f"{topping['DMG_Resist']:<10.1f}")
    print("-" * 50)
    
    # Stats comparison
    print(f"\nStats Comparison (Current -> New):")
    print("-" * 50)
    print(f"{'ATK:':<20}{current_atk:.2f} -> {total_atk:.2f} ({total_atk - current_atk:+.2f})")
    print(f"{'Cooldown:':<20}{current_cooldown:.2f} -> {total_cooldown:.2f} ({total_cooldown - current_cooldown:+.2f})")
    print(f"{'DMG_Resist:':<20}{current_dmg_resist:.2f} -> {total_dmg_resist:.2f} ({total_dmg_resist - current_dmg_resist:+.2f})")
else:
    print("No valid combination found.")