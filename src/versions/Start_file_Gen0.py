from Gen0 import Individ, Population

POP_QUANT = 6 # количество поколений

BESTIES = []
population = Population() 
population.create_new() # создание первой популяции и первых индивидоа

for i in range(POP_QUANT): # цикл смены поколений
    population.population_fight() # "бои" / попарное сравнение
    population.create_childs() # создание потомства
    population.print_data(all=1) # вывод данных о популяции
    BESTIES.append(population.get_best()) # добавление лучшего индивида в список лучших 
    print('POPULATION QUALITY:', population.get_pop_quality()) # make grafic
    print('------------NEW GENERATION----------------')
    population = population.create_pop_from_childs() # Переинициализация потомков во взрослых

# for i in range(len(BESTIES)):
#     print(BESTIES[i].get_data())
print('BEST EVER: ', max(BESTIES).get_data())