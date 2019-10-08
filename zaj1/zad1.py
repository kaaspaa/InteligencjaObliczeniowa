from operator import add, mul
import numpy as np
import random
import math
#a)
print("a) Oblicz ile to jest 45*678")
print("odp = ", 45*678,"\n")

#b)
print("b) Wczytaj pod zmienne dwa wektory: x=(7; 4; 2; 0; 9) oraz y=(2; 1; 5; 3; 3).")
x = [7,4,2,0,9]
y = [2,1,5,3,3]
print("x = ",x)
print("y = ",y, "\n")

#c)
print("c)Oblicz za pomocą jednej operacji wektor, którego współrzędne są sumami współrzędnych wektorów x i y. Wyświetl ten wektor.")
print("odp = ", list(map(add,x,y)), "\n")

#d)
print("d)Oblicz w podobny sposób iloczyn y współrzędnych wektorów.")
print("odp = ", list(map(mul,x,y)), "\n")

#e)
print("e)Oblicz za pomocą mnożenia macierzowego iloczyn skalarny wektorów (wynik to liczba będąca sumą iloczynów współrzędnych).")
pom = list(map(mul,x,y))
odp_e = 0
for i in pom:
    odp_e += i
print("odp = ",odp_e,"\n")

#f)
print("f)Oblicz iloczyn macierzy korzystając z mnożenia macierzowego.\n"
        ," _     _   _     _\n"
        ," |0,2,1|   |9,8,7|\n"
        ," |1,6,4|   |1,2,7|\n"
        ," |5,0,3|   |4,9,2|\n"
        ," ‾     ‾   ‾     ‾")
A = np.array([[0,2,1], [1,6,4], [5,0,3]])
B = np.array([[9,8,7], [1,2,7], [4,9,2]])
odp_f = A*B
print(odp_f,"\n")

#g)
print("g)Wygeneruj za pomocą odpowiedniej komendy wektor z liczbami od 1 do 100.")
arr_g = []
for i in range(100):
    arr_g.append(i+1)
print("wektor:")
print(arr_g,"\n\n")

#h)
print("(h)Oblicz sumę, średnią, odchylenie standardowe tych liczb za pomocą odpowiednich komend.")
sum_h = 0
for i in arr_g:
    sum_h += i
print("suma = ", sum_h)

avg_h = sum_h/len(arr_g)
print("srednia = ", avg_h)

auxiliary_var = 0
for i in arr_g:
    auxiliary_var += (i - avg_h)**2
stnd_dev_h = math.sqrt((auxiliary_var)/len(arr_g))
print("odchyelnie standardowe = ", stnd_dev_h)

#i)
print("i)Wygeneruj za pomocą odpowiedniej komendy wektor z 20 losowymi liczbami od 0 do 50.")
help_array = np.random.randint(51,size = 20)
print(help_array,"\n")

#j)
print("j) Oblicz min i max z tych losowych liczb za pomocą odpowiednich komend.")
print("min = ",min(help_array))
print("max = ",max(help_array))
