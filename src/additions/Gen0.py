from random import choices, shuffle, randint
from Funcs import pairwise

class Individ:
    def __init__(self, params=None):
        self.params = []
        if not params:
            self.params = choices([0, 1], k=IND_LENTH)
        else:
            self.params = params
            # print(self.params)
        self.quantity = sum(self.params)
    
    def get_data(self):
        return self.params, self.quantity

    def __lt__(self, other):
        print((self.get_data())[1], (other.get_data())[1])
        return (self.get_data())[1] < (other.get_data())[1]

    def __gt__(self, other):
        print((self.get_data())[1], (other.get_data())[1])
        return (self.get_data())[1] > (other.get_data())[1]

class Population:
    def __init__(self) -> None:
        self.individs = {} # every ind: {number: object}
        self.parents = {}
        self.childs = {}
        self.best = None
        if len(self.individs) > 0:
            self.best = self.get_best()
    def create_new(self):
        for i in range(POP_LENTH):
            self.individs[i] = Individ()
        self.best = self.get_best()



    def population_fight(self):
        order = [i for i in range(len(self.individs))]
        shuffle(order)
        winner_list = []
        for i, j in pairwise(order):
            if j != None:
                i_winner = self.local_fight(i, j)
                obj_winner = self.individs[i_winner]
                winner_list.append(obj_winner)
            else:
                winner_list.append(self.individs[i])
            # print((obj_winner.get_data())[0])
            # print((self.individs[i].get_data())[1], (self.individs[j].get_data())[1])
        for i in range(len(winner_list)):
            self.parents[i] = winner_list[i]
        self.best = self.get_best()


    
    def local_fight(self, i1, i2): # i1 and i2 = i in cycle with step=2
        # print(f'''{(self.individs[i1].get_data())} qual = {(self.individs[i1].get_data())[1]} i = {i1}
        # \n {(self.individs[i2].get_data())} - qual = {(self.individs[i2].get_data())[1]} i = {i2}''')
        if (self.individs[i1].get_data())[1] > (self.individs[i2].get_data())[1]:
            return i1
        return i2

    def print_data(self, individs=None, parents=None, childs=None, best=None):
        if individs:
            for i in range(len(self.individs)):
                print(self.individs[i].get_data())
        if parents:
            for i in range(len(self.parents)):
                print(self.parents[i].get_data())
        if childs:
            for i in range(len(self.childs)):
                print(self.childs[i].get_data())
        if best:
            print('BEST:', self.best.get_data())

    def create_childs(self):
        order = [i for i in range(len(self.parents))]
        shuffle(order)
        # print(order)
        cut_place = randint(0, IND_LENTH)
        dicts_i1 = 0
        dicts_i2 = dicts_i1 + 1
        for i, j in pairwise(order):
            if j != None:
                parent1, parent2 = self.parents[i], self.parents[j]
                part1 = ((parent1.get_data())[0])[:cut_place]
                part2 = ((parent2.get_data())[0])[cut_place:]
                child1 = part1 + part2 # its a list, not obj
                child2 = ((parent2.get_data())[0])[:cut_place] + ((parent1.get_data())[0])[cut_place:] # its a list, not obj
                # print('1-:', child1)
                # print('2-:', child2)
                self.childs[dicts_i1] = child1
                self.childs[dicts_i2] = child2
                dicts_i1 += 2
                dicts_i2 += 2
            else: # if its 1 parent at the end
                child1 = (((self.parents[i]).get_data())[0])
                # print('1+:', child1)
                # print('2+:', child2)
                self.childs[dicts_i1] = child1



            # add childs as obj of INDIVID class, add them quantity

    def create_pop_from_childs(self):
        pop2 = Population()
        self.best = self.get_best()
        for i, child in self.childs.items():
            pop2.individs[i] = Individ(child)
            i += 1
        return pop2

    
    def get_best(self):
        return  self.individs[max(self.individs, key=self.individs.get)]



IND_LENTH = 10
POP_LENTH = 10
pop1 = Population()
pop1.create_new()
# pop1.print_data(individs=1)
pop1.population_fight()
pop1.create_childs()
# print(111111111111)
pop2 = pop1.create_pop_from_childs()
pop2.population_fight()
pop2.print_data(parents=1, best=1)
pop2.create_childs()
pop3 = pop2.create_pop_from_childs()

