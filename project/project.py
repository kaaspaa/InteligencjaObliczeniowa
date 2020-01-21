from algorithmA import *
from fitnessAlgorithm import *

maze = [(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0),
        (0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0),
        (0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0), (0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0),
        (0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0),
        (0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0), (0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0),
        (0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0),
        (0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0), (0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)]

start = [1, 1]
end = [10, 10]

AStarPath = givePath(maze, start, end)
for i in AStarPath:
    print(i)
length = len(AStarPath[1]) * 2
print("dlugosc sciezki A*")
print(length / 2)
print("fitness:")
fitness_val_1 = giveBestFitnessValue(maze, start, end, length, 1)
for i in fitness_val_1:
        print(i)
fitness_path_1 = make_path_out_of_chrom(maze, fitness_val_1)
print(fitness_path_1)

print("fitness 2:")
fitness_val_2 = giveBestFitnessValue(maze, start, end, length, 2)
for i in fitness_val_2:
        print(i)
fitness_path_2 = make_path_out_of_chrom(maze, fitness_val_2)
print(fitness_path_2)
