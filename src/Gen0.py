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
        self.parents = {}
        self.childs = {}

    def create(self):
        for i in range(POP_LENTH):
            self.individs[i] = Individ()

    # def population_fight(self):
    #     order = shuffle([i for i in range(POP_LENTH)])
    #     for i in range(POP_LENTH // 2):
            pass

    def population_fight(self):
        order = [i for i in range(POP_LENTH)]
        shuffle(order)
        winner_list = []
        for i in range(0, len(order), 2):
            #print(order[i], order[i + 1])
            i_winner = self.local_fight(i, i + 1)
            # print(i_winner)
            obj_winner = self.individs[i_winner]
            winner_list.append(obj_winner)
        if len(order) % 2 != 0: # if col of inds is odd, we add last individ without couple
            winner_list.append(self.individs[-1])
        for i in range(len(winner_list)):
            self.parents[i] = winner_list[i]


    
    def local_fight(self, i1, i2): # i1 and i2 = i in cycle with step=2
        # print(f'''{(self.individs[i1].get_data())} qual = {(self.individs[i1].get_data())[1]} i = {i1}
        # \n {(self.individs[i2].get_data())} - qual = {(self.individs[i2].get_data())[1]} i = {i2}''')
        if (self.individs[i1].get_data())[1] > (self.individs[i2].get_data())[1]:
            return i1
        return i2

    def print_data(self):
        for i in range(len(self.parents)):
            # print(self.individs[i].get_data())
            # print((self.individs[i].get_data())[1])
            print(self.parents[i].get_data())

    def create_childs(self):
        pass


IND_LENTH = 10
POP_LENTH = 10
pop1 = Population()
pop1.create()
pop1.population_fight()
pop1.print_data()

