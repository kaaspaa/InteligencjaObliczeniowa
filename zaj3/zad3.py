from pyeasyga import pyeasyga
import random


def fitness(chrom, maze):
    fitness = 0
    start = [1, 1]
    finish = [10, 10]
    temp = [[0 for i in range(12)] for y in range(12)]
    for i in range(len(chrom)):
        if chrom[i] == 1:#idzie w lewo
            if maze[start[0]][start[1] - 1] == 1:
                start[1] -= 1
        if chrom[i] == 2:#idzie w prawo
            if maze[start[0]][start[1] + 1] == 1:
                start[1] += 1
        if chrom[i] == 3:#idzie w dol
            if maze[start[0] + 1][start[1]] == 1:
                start[0] += 1
        if chrom[i] == 4:#idzie w gore
            if maze[start[0] - 1][start[1]] == 1:
                start[0] -= 1
        if start == finish:
            fitness = 100
            return fitness
        else:
            fitness = 2*start[0] + start[1]
    return fitness


def generate_chrom(data):
    chrom = []
    for i in range(40):
        chrom.append(random.randint(1, 4))
    return chrom


maze = [(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0),
        (0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0),
        (0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0), (0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0),
        (0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0),
        (0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0), (0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0),
        (0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0),
        (0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0), (0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)]
ga = pyeasyga.GeneticAlgorithm(maze,
                               population_size=300,
                               generations=150,
                               crossover_probability=0.8,
                               mutation_probability=0.1,
                               elitism=True,
                               maximise_fitness=True)
ga.create_individual = generate_chrom
ga.fitness_function = fitness
ga.run()
print(ga.best_individual())
