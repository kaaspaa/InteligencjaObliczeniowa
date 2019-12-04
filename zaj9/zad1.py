import math


def fct_act(val):
    final_val = 1/(1 + (math.exp(-val)))
    return final_val


def forwardPass(wiek, waga, wzrost):
    n1 = 0
    n2 = 0
    nfinal = 0
    weights = [-0.46122, 0.78548, 0.97314, 2.10584, -0.39203, -0.57847, -0.81546, 1.03775]
    biases = [0.80109, 0.43529, -0.2368]
    n1 += wiek*weights[0] + waga*weights[2] + wzrost*weights[4] + biases[0]
    n2 += wiek*weights[1] + waga*weights[3] + wzrost*weights[5] + biases[1]
    nfinal += fct_act(n1)*weights[6] + fct_act(n2)*weights[7] + biases[2]
    return nfinal


wiek = 23
waga = 75
wzrost = 176
score = forwardPass(wiek, waga, wzrost)
print("score 1:")
print(score)
score = forwardPass(wiek=25, waga=67, wzrost=180)
print("score 2:")
print(score)
score = forwardPass(wiek=28, waga=120, wzrost=175)
print("score 3:")
print(score)
