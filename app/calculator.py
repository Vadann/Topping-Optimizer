from models.topping import Topping
from itertools import combinations

class Calculator:
    def __init__(self, toppings_data):
        self.toppings = [Topping(data) for data in toppings_data]
    def addToppings(self, topping):
        if not isinstance(topping, Topping):
            raise TypeError(f"Expected of type topping, but got {type(topping).__name__}")
        self.toppings.append(topping)

    def getToppings(self):
        return self.toppings

    # Calculate the total of the base stats for the toppings
    # Works based on the chosed combination of 5 topping, hel[ful when checking every possible combination.
    def calculateBaseTotal(self, topping_set):

        topping_map = {}

        for topping in topping_set:
            print(topping.type)
            if topping.type in topping_map:
                print(topping.getBaseStat())
                topping_map[topping.type] += topping.getBaseStat()
            else:
                print("Added Unknown Element")
                topping_map[topping.type] = topping.getBaseStat()

        return list(topping_map.values())  # Loop through a range (up to 'amount' times)

    def find_best_toppings(self, stat1, stat2, stat3, stat_ranges=None, priority_order=None):




topping_data = [
    {'type': 'raspberry', 'ATK': 3, 'Crit': 2.6, 'ATK_SPD': 2.3},
    {'type': 'raspberry', 'ATK': 2.6, 'Crit': 2.9, 'ATK_SPD': 1.1},
    {'type': 'raspberry', 'ATK': 2.9, 'Crit': 1.3, 'ATK_SPD': 2.3},
    {'type': 'raspberry', 'ATK': 2.7, 'Crit': 0.0, 'ATK_SPD': 2.9},
    {'type': 'raspberry', 'ATK': 2.3, 'Crit': 1.3, 'ATK_SPD': 0},
    {'type': 'raspberry', 'ATK': 2.2, 'Crit': 1.0, 'ATK_SPD': 0},
    {'type': 'raspberry', 'ATK': 2.3, 'Crit': 0.0, 'ATK_SPD': 3.0},
    {'type': 'raspberry', 'ATK': 0, 'Crit': 2.1, 'ATK_SPD': 2.9},
    {'type': 'raspberry', 'ATK': 2.9, 'Crit': 0.0, 'ATK_SPD': 2.4},
    {'type': 'raspberry', 'ATK': 1.2, 'Crit': 2, 'ATK_SPD': 2.2},
    {'type': 'raspberry', 'ATK': 0, 'Crit': 2.6, 'ATK_SPD': 1.7},
    {'type': 'raspberry', 'ATK': 2.8, 'Crit': 2.8, 'ATK_SPD': 0},
    {'type': 'raspberry', 'ATK': 2.4, 'Crit': 2.8, 'ATK_SPD': 0},
    {'type': 'raspberry', 'ATK': 0, 'Crit': 2.6, 'ATK_SPD': 2.2},
    {'type': 'raspberry', 'ATK': 2.4, 'Crit': 2.4, 'ATK_SPD': 0.0},
    {'type': 'raspberry', 'ATK': 0.0, 'Crit': 2.4, 'ATK_SPD': 3.0},
    {'type': 'raspberry', 'ATK': 2.7, 'Crit': 2.2, 'ATK_SPD': 0.0},
    {'type': 'raspberry', 'ATK': 2.8, 'Crit': 0.0, 'ATK_SPD': 2.5},
    {'type': 'apple_jelly', 'ATK': 1.7, 'Crit': 2.0, 'ATK_SPD': 1.8},
    {'type': 'apple_jelly', 'ATK': 1.7, 'Crit': 2.6, 'ATK_SPD': 1.7},
    {'type': 'apple_jelly', 'ATK': 1.7, 'Crit': 2.0, 'ATK_SPD': 1.2},
    {'type': 'apple_jelly', 'ATK': 2.8, 'Crit': 2.5, 'ATK_SPD': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.8, 'Crit': 2.3, 'ATK_SPD': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.3, 'Crit': 1.8, 'ATK_SPD': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.2, 'Crit': 1.9, 'ATK_SPD': 0},
    {'type': 'apple_jelly', 'ATK': 2.2, 'Crit': 0.0, 'ATK_SPD': 1.6},
    {'type': 'apple_jelly', 'ATK': 2.2, 'Crit': 2.8, 'ATK_SPD': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.4, 'Crit': 0.0, 'ATK_SPD': 2.3},
    {'type': 'apple_jelly', 'ATK': 1.3, 'Crit': 0.0, 'ATK_SPD': 2.3},
    {'type': 'apple_jelly', 'ATK': 1.2, 'Crit': 0.0, 'ATK_SPD': 2.3},
    {'type': 'apple_jelly', 'ATK': 2.3, 'Crit': 0.0, 'ATK_SPD': 2.0},
    {'type': 'apple_jelly', 'ATK': 1.1, 'Crit': 0.0, 'ATK_SPD': 2.0},
    {'type': 'apple_jelly', 'ATK': 1.6, 'Crit': 0.0, 'ATK_SPD': 1.4},
    {'type': 'apple_jelly', 'ATK': 0.0, 'Crit': 2.9, 'ATK_SPD': 1.4},
    {'type': 'apple_jelly', 'ATK': 0.0, 'Crit': 2.9, 'ATK_SPD': 2.1},
    {'type': 'apple_jelly', 'ATK': 2.9, 'Crit': 2.8, 'ATK_SPD': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'Crit': 2.8, 'ATK_SPD': 1.4},
    {'type': 'apple_jelly', 'ATK': 0.0, 'Crit': 2.7, 'ATK_SPD': 1.2},
    {'type': 'apple_jelly', 'ATK': 2.4, 'Crit': 2.4, 'ATK_SPD': 2.3},
    {'type': 'apple_jelly', 'ATK': 1.3, 'Crit': 2.3, 'ATK_SPD': 0.0},
    {'type': 'apple_jelly', 'ATK': 2.0, 'Crit': 2.3, 'ATK_SPD': 0.0},
    {'type': 'apple_jelly', 'ATK': 1.9, 'Crit': 2.1, 'ATK_SPD': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'Crit': 1.7, 'ATK_SPD': 1.7},
    {'type': 'apple_jelly', 'ATK': 0.0, 'Crit': 1.2, 'ATK_SPD': 2.0},
    {'type': 'apple_jelly', 'ATK': 1.6, 'Crit': 1.1, 'ATK_SPD': 0.0},
    {'type': 'apple_jelly', 'ATK': 0.0, 'Crit': 1.1, 'ATK_SPD': 2.5},
    {'type': 'apple_jelly', 'ATK': 0.0, 'Crit': 2.4, 'ATK_SPD': 1.8},
]

calc = Calculator(topping_data)

best_combo, max_stats = calc.find_best_toppings("raspberry", ["ATK", "Crit", :])