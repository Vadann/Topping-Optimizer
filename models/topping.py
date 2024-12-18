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
        if stats is None:
            self.stats = {}
        else:
            self.stats = stats

        self.type = stats["type"]

    def __repr__(self):
        key_list = list(self.stats.keys())
        stat_list = []

        for key in key_list:
            if key != "type":
                stat_list.append(key)

        return f"Topping: {self.type} {stat_list[0]}: {self.stats[stat_list[0]]} {stat_list[1]}: {self.stats[stat_list[1]]} {stat_list[2]}: {self.stats[stat_list[2]]} "


    def getType(self):
        return self.type

    def getStats(self):
        return self.stats

    def getBaseStat(self):
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
                    return value

    def setStat(self, stats):
        self.stats = stats

