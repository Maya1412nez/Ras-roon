from Gen0 import Individ, Population


IND_LENTH = 10
POP_LENTH = 60
POP_QUANT = 6

BESTIES = []
population = Population()
population.create_new()

for i in range(POP_QUANT):
    population.population_fight()
    population.create_childs()
    population.print_data(all=1)
    BESTIES.append(population.get_best())
    print('POPULATION QUALITY:', population.get_pop_quality()) # make grafic
    print('------------NEW GENERATION----------------')
    population = population.create_pop_from_childs()

# for i in range(len(BESTIES)):
#     print(BESTIES[i].get_data())
print('BEST EVER: ', max(BESTIES).get_data())