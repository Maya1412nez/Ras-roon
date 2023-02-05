from random import choices, shuffle, randint
from Funcs import pairwise


class Individ:
    def __init__(self, params=None):
        self.params = []
        if not params:
            self.params = choices([0, 1], k=IND_LENTH)
        else:
            self.params = params
        self.quantity = sum(self.params)

    def get_data(self):
        return self.params, self.quantity

    def __lt__(self, other):
        # print((self.get_data())[1], (other.get_data())[1])
        return (self.get_data())[1] < (other.get_data())[1]

    def __gt__(self, other):
        # print((self.get_data())[1], (other.get_data())[1])
        return (self.get_data())[1] > (other.get_data())[1]


class Population:
    def __init__(self) -> None:
        self.individs = {}  # every ind: {number: object}
        self.parents = {}
        self.childs = {}
        self.best = None
        if len(self.individs) > 0:
            self.best = self.get_best()
        self.quality = 0

    def create_new(self, all_params=None):
        if not all_params:
            for i in range(POP_LENTH):
                self.individs[i] = Individ()
        else:
            for i in range(len(all_params)):
                self.individs[i] = Individ(all_params[i])
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

    def local_fight(self, i1, i2):  # i1 and i2 = i in cycle with step=2
        # print(f'''{(self.individs[i1].get_data())} qual = {(self.individs[i1].get_data())[1]} i = {i1}
        # \n {(self.individs[i2].get_data())} - qual = {(self.individs[i2].get_data())[1]} i = {i2}''')
        if (self.individs[i1].get_data())[1] > (self.individs[i2].get_data())[1]:
            return i1
        return i2

    def print_data(self, individs=None, parents=None, childs=None, best=None, all=None):
        if individs or all:
            for i in range(len(self.individs)):
                print(f'INDIVID {i}', self.individs[i].get_data())
        if parents or all:
            for i in range(len(self.parents)):
                print(f'PARENT  {i}', self.parents[i].get_data())
        if childs or all:
            for i in range(len(self.childs)):
                print(f'CHILD   {i}', self.childs[i].get_data())
        if best or all:
            print('BEST:    ', self.best.get_data())

    def create_childs(self):
        order = [i for i in range(len(self.parents))]
        shuffle(order)
        cut_place = randint(0, IND_LENTH)
        dicts_i1 = 0
        dicts_i2 = dicts_i1 + 1
        for i, j in pairwise(order):
            if j != None:
                parent1, parent2 = self.parents[i], self.parents[j]
                part1 = ((parent1.get_data())[0])[:cut_place]
                part2 = ((parent2.get_data())[0])[cut_place:]
                child1 = part1 + part2  # its a list, not obj
                child2 = ((parent2.get_data())[0])[:cut_place] + ((parent1.get_data())[0])[
                    cut_place:]  # its a list, not obj
                # print('1-:', child1)
                # print('2-:', child2)
                self.childs[dicts_i1] = Individ(child1)
                self.childs[dicts_i2] = Individ(child2)
                dicts_i1 += 2
                dicts_i2 += 2
            else:  # if its 1 parent at the end
                child1 = (((self.parents[i]).get_data())[0])
                # print('1+:', child1)
                # print('2+:', child2)
                self.childs[dicts_i1] = Individ(child1)

    def create_pop_from_childs(self):
        pop2 = Population()
        self.best = self.get_best()
        for i, child in self.childs.items():
            pop2.individs[i] = child
            i += 1
        return pop2

    def get_pop_quality(self):
        sum_qual = 0
        for i in range(len(self.individs)):
            sum_qual += ((self.individs[i]).get_data())[1]
        self.quality = sum_qual / len(self.individs)
        return self.quality

    def get_best(self):
        return self.individs[max(self.individs, key=self.individs.get)]


try:
    from Gen1_1_1 import IND_LENTH, POP_LENTH, POP_QUANT
except:
    IND_LENTH = 10
    POP_LENTH = 60
    POP_QUANT = 6
# IND_LENTH = 10
# POP_LENTH = 60
# POP_QUANT = 6


# BESTIES = []
# population = Population()
# population.create_new()

# for i in range(POP_QUANT):
#     population.population_fight()
#     population.create_childs()
#     population.print_data(all=1)
#     BESTIES.append(population.get_best())
#     print('POPULATION QUALITY:', population.get_pop_quality()) # make grafic
#     print('------------NEW GENERATION----------------')
#     population = population.create_pop_from_childs()

# # for i in range(len(BESTIES)):
# #     print(BESTIES[i].get_data())
# print('BEST EVER: ', max(BESTIES).get_data())
