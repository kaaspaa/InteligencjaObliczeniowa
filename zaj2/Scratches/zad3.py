import random
import matplotlib.pyplot as plt

vector = []
for i in range(100):
    vector.append(random.randint(0,20))
n_counter = []
for i in range(0,21):
    n_counter.append(0)
numbers = list(range(0,21))
for i in range(100):
    n_counter[vector[i]] += 1
for i in range(21):
    print("ilosc liczb '", i, "' wynosi: ", n_counter[i])

plt.bar(numbers, n_counter, align='center')
plt.xlabel('liczba')
plt.ylabel('liczba wystapien')
plt.title('random.randint graph')
plt.show()