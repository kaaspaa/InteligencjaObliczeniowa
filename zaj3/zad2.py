import random
import matplotlib.pyplot as plt
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

gen = 1
bests = []
meds = []
for i in range(5):
    best = 0
    med = 0
    ga = pyeasyga.GeneticAlgorithm(mylist,
                                   population_size=20,
                                   generations=gen,
                                   crossover_probability=0.8,
                                   mutation_probability=0.1,
                                   elitism=True,
                                   maximise_fitness=True)
    ga.fitness_function=fitness
    ga.run()
    gen += 1
    best += ga.best_individual()[0]
    bests.append(best)
    for individual in ga.last_generation():
        med += individual[0]
    meds.append(med/ga.population_size)
print("bests = " + str(bests))
print("\nmeds = " + str(meds))

x = [1,2,3,4,5]
plt.plot(x,bests)
plt.plot(x,meds)
plt.xlabel('Generations')
plt.ylabel('Value')
plt.title('Graph graph')
plt.show()
