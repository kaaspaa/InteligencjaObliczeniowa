import random
from pyeasyga import pyeasyga


def fitness(chrom, data):
    fitness = 0
    result = 0
    for clause in data:
        for i in clause:
            var = abs(i) - 1
            if i > 0:
                result |= chrom[var]
            else:
                result |= not chrom[var]
        fitness += result
    return fitness


data = [[-1, 2, 4],
        [-2, 3, 4],
        [1, -3, 4],
        [1, -2, -4],
        [2, -3, -4],
        [2, -3, -4],
        [-1, 3, -4],
        [1, 2, 3]]

ga = pyeasyga.GeneticAlgorithm(data,
                               population_size=200,
                               generations=500,
                               crossover_probability=0.8,
                               mutation_probability=0.1,
                               elitism=True,
                               maximise_fitness=True)
ga.fitness_function = fitness
ga.run()
print(ga.best_individual())