from pyeasyga import pyeasyga
import random


def fitness_type_1(chrom, maze):
    start = [1, 1]
    finish = [10, 10]
    for i in range(len(chrom)):
        if chrom[i] == 1:  # idzie w lewo
            if maze[start[0]][start[1] - 1] == 1:
                start[1] -= 1
            else:
                break
        if chrom[i] == 2:  # idzie w prawo
            if maze[start[0]][start[1] + 1] == 1:
                start[1] += 1
            else:
                break
        if chrom[i] == 3:  # idzie w dol
            if maze[start[0] + 1][start[1]] == 1:
                start[0] += 1
            else:
                break
        if chrom[i] == 4:  # idzie w gore
            if maze[start[0] - 1][start[1]] == 1:
                start[0] -= 1
            else:
                break
        if start == finish:
            fitness = 0
            return fitness
    fitness = (abs(finish[0] - start[0]) + abs(finish[1] - start[1]))
    return fitness


def fitness_type_2(chrom, maze):
    start = [1, 1]
    finish = [10, 10]
    for i in range(len(chrom)):
        if chrom[i] == 1:  # idzie w lewo
            if maze[start[0]][start[1] - 1] == 1:
                start[1] -= 1
        if chrom[i] == 2:  # idzie w prawo
            if maze[start[0]][start[1] + 1] == 1:
                start[1] += 1
        if chrom[i] == 3:  # idzie w dol
            if maze[start[0] + 1][start[1]] == 1:
                start[0] += 1
        if chrom[i] == 4:  # idzie w gore
            if maze[start[0] - 1][start[1]] == 1:
                start[0] -= 1
        if start == finish:
            fitness = 0
            return fitness
    fitness = (abs(finish[0] - start[0]) + abs(finish[1] - start[1]))
    return fitness


# na razie zignorowac
def fitness_type_3(chrom, maze):
    fitness = 0
    start = [1, 1]
    finish = [10, 10]
    for i in range(len(chrom)):
        if chrom[i] == 1:  # idzie w lewo
            if maze[start[0]][start[1] - 1] == 1:
                start[1] -= 1
        if chrom[i] == 2:  # idzie w prawo
            if maze[start[0]][start[1] + 1] == 1:
                start[1] += 1
        if chrom[i] == 3:  # idzie w dol
            if maze[start[0] + 1][start[1]] == 1:
                start[0] += 1
        if chrom[i] == 4:  # idzie w gore
            if maze[start[0] - 1][start[1]] == 1:
                start[0] -= 1
        if start == finish:
            fitness = 100
            return fitness
        else:
            fitness = 2 * start[0] + start[1]
    return fitness


# pyeasyga potrzebuje jednego argumentu w metodzie create_individual
def generate_chrom(data):
    chrom = []
    for i in range(40):
        chrom.append(random.randint(1, 4))
    return chrom


# na razie zignorowac. Bedzie przydatne do funkcji fitness 3
def generate_chrom_vec(data):
    chrom = []
    length = 0
    for line in data:
        for x in line:
            if x == 1:
                length += 1
    for i in range(length):
        chrom.append(random.randint(1, 2))
    return chrom


# maze: 0 - sciana, 1 - wolna sciezka.
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
                               generations=200,
                               crossover_probability=0.8,
                               mutation_probability=0.1,
                               elitism=True,
                               maximise_fitness=False)
ga.create_individual = generate_chrom
ga.fitness_function = fitness_type_1
ga.run()
best_1 = ga.best_individual()

ga.fitness_function = fitness_type_2
ga.run()
best_2 = ga.best_individual()

print("Najlepszy wynik dla funkcji fitness 1:")
print(best_1)
print("Najlepszy wynik dla funkcji fitness 2:")
print(best_2)
