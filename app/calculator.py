from models.topping import Topping
from itertools import combinations

class Calculator:
    def __init__(self, toppings=None):
        self.toppings = toppings or []

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

    def findBestToppings(self, stat1=None, stat2=None, stat3=None, stat1_range=None, stat2_range=None, stat3_range=None, priority=None):

        toppings = self.getToppings()
        stats_by_topping = [
            {
                stat1: topping.getStatsByAttribute(stat1),
                stat2: topping.getStatsByAttribute(stat2),
                stat3: topping.getStatsByAttribute(stat3)
            }
            for topping in toppings
        ]

        best_combination = None
        best_stat1_total = 0
        best_stat2_total = 0
        best_stat3_total = 0

        for topping_combination in combinations(stats_by_topping, 5):
            stat1_total = sum(topping[stat1] for topping in topping_combination if stat1)
            stat2_total = sum(topping[stat2] for topping in topping_combination if stat2)
            stat3_total = sum(topping[stat3] for topping in topping_combination if stat3)

            if stat1_total + stat2_total + stat3_total > best_stat1_total + best_stat2_total + best_stat3_total:
                best_combination = topping_combination
                best_stat1_total = stat1_total
                best_stat2_total = stat2_total
                best_stat3_total = stat3_total

        return best_combination



calc = Calculator()

#print(calc.getToppings())

topping1 = Topping({'type': 'raspberry', 'ATK': 2.8, 'Crit': 0.0, 'ATK_SPD': 2.5})
topping2 = Topping({'type': 'apple_jelly', 'ATK': 1.7, 'Crit': 2.0, 'ATK_SPD': 1.8})
topping3 = Topping({'type': 'raspberry', 'ATK': 2.8, 'Crit': 0.0, 'ATK_SPD': 2.5})
topping4 = Topping({'type': 'apple_jelly', 'ATK': 1.7, 'Crit': 2.0, 'ATK_SPD': 1.8})
topping5 = Topping({'type': 'raspberry', 'ATK': 2.8, 'Crit': 0.0, 'ATK_SPD': 2.5})

# List of all Topping objects
toppings_list = [topping1, topping2, topping3, topping4, topping5]

for topping in toppings_list:
    calc.addToppings(topping)

print(calc.getToppings())

print(calc.calculateBaseTotal(toppings_list))

topping1.getStatsByAttribute("Crit")


calc.findBestToppings("ATK", "Crit", "ATK_SPD")