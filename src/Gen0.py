from random import choices, shuffle


class Individ:
    def __init__(self) -> None:
        self.params = choices([0, 1], k=IND_LENTH)
        self.quantity = sum(self.params)
    
    def get_data(self):
        return self.params, self.quantity

class Population:
    def __init__(self) -> None:
        self.individs = {} # every ind: {number: object}
        self.childs = {}

    def create(self):
        for i in range(POP_LENTH):
            self.individs[i] = Individ()

    def population_fight(self):
        order = shuffle([i for i in range(POP_LENTH)])
        for i in range(POP_LENTH // 2):
            pass
    
    def local_fight(self, num1, num2):
        if self.individs[num1].get_data[0] > self.individs[num2].get_data[0]:
            return num1
        return num2


IND_LENTH = 10
POP_LENTH = 10
individ = Individ()
