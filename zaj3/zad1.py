import random
from pyeasyga import pyeasyga

mylist = [("zegar", 100, 7), ("obraz-prejzaz", 300, 7), ("obraz-portret", 200, 6), ("radio", 40, 2),
("laptop", 500, 5), ("lampka nocna", 70, 6), ("srebrne sztucce", 100, 1), ("porcelana", 250, 3),
("figura z brazu", 300, 10), ("skorzana torebka", 280, 3), ("odkurzacz", 300, 15)]


def fitness(chrom,mylist):
    value = 0
    weight = 0
    for i in range(len(chrom)):
        if chrom[i] == 1:
            value += mylist[i][1]
            weight += mylist[i][2]
    if weight > 25:
        return 0
    else:
        return value


def generate_chrom():
    chrom = []
    for i in range(11):
        chrom.append(random.randint(0, 1))
    return chrom


print(mylist)
list_of_chroms = []
for i in range(200):
    list_of_chroms.append(generate_chrom())

ga = pyeasyga.GeneticAlgorithm(mylist,
                               population_size=200,
                               generations=100,
                               crossover_probability=0.8,
                               mutation_probability=0.1,
                               elitism=True,
                               maximise_fitness=True)
ga.fitness_function=fitness
ga.run()
print(ga.best_individual())
#print("some values:\n")