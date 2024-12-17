from models.topping import Topping


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
                print(topping.getBaseStats())
                topping_map[topping.type] += topping.getBaseStats()
            else:
                print("Added Unknown Element")
                topping_map[topping.type] = topping.getBaseStats()

        return list(topping_map.values())  # Loop through a range (up to 'amount' times)


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
