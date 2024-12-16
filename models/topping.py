class Topping:
    counter = 1

    baseToppings = {
        "raspberry": 9,
        "chocolate": 3,
        "caramel": 4.1,
        "apple_jelly": 9
    }



    def __init__(self, stats=None):
        self.id = Topping.counter
        Topping.counter += 1
        self.type = type
        if stats is None:
            self.stats = {}
        else:
            self.stats = stats

        self.type = stats["type"]

    def __repr__(self):
        return f"Topping(type={self.type}, ATK={self.stats["ATK"]}, Crit={self.stats["Crit"]}, ATK_SPD={self.stats["ATK_SPD"]})"

    def getType(self):
        return self.type

    def getStats(self):
        return self.stats

    def getBaseStats(self):
        if self.type in Topping.baseToppings:
            return Topping.baseToppings[self.type]

    def getStatsByAttribute(self, attribute):
        if not isinstance(attribute, list):
            attributes = [attribute]
        else:
            attributes = attribute

        for attribute in attributes:
            for key, value in self.stats.items():
                if key == attribute:
                    print(f"Key {key} found with value {value}")

    def setStat(self, stats):
        self.stats = stats
