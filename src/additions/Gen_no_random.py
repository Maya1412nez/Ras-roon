from random import choices, shuffle


class Individ:
    def __init__(self, params=None) -> None:            # changed
        if not params:                                  # changed
            self.params = choices([0, 1], k=IND_LENTH)  # changed
        else:                                           # changed
            self.params = list(params) # changed
            print('llllllll', (self.params))
        self.quantity = sum(self.params)
    
    def get_data(self):
        return self.params, self.quantity

class Population:
    def __init__(self) -> None:
        self.individs = {} # every ind: {number: object}
        self.childs = {}
        self.best = None

    def create(self, params=None):                      # changed
        print(params)
        for i in range(POP_LENTH): 
            self.individs[i] = Individ(params[i])

    def population_fight(self):
        order = [i for i in range(POP_LENTH)]
        shuffle(order)
        winners = {}
        j = 0
        print(order)
        for i in range(0, POP_LENTH, 2):
            winners[j] = self.local_fight(order[i], order[i + 1])
            print(order[i], order[i + 1], winners[j].get_data[0])
            j += 1
    
    def local_fight(self, num1, num2):
        print((self.individs[num1].get_data()))
        if (self.individs[num1].get_data())[1] > (self.individs[num2].get_data())[1]:
            return num1
        return num2

    def get_pop_data(self):
        return self.individs


IND_LENTH = 5                                            # changed
POP_LENTH = 5                                            # changed

ind = Individ([1, 0, 1, 0, 1])
print(ind.get_data())
pop1 = Population()
pararams = ['000000', '00001', '00011', '00111', '01111', '11111']
pop1.create(params=pararams)
pop1.population_fight()


