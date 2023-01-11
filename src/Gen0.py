from random import choices


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

    def fight(self):
        pass


IND_LENTH = 10
POP_LENTH = 10
individ = Individ()
