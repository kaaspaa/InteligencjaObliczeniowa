import numpy as np
import math

def function(v1,v2):
    vec1_l = 0
    vec2_l = 0
    skalar = 0
    for index in range(len(v1)):
        skalar += v1[index] * v2[index]
        vec1_l += v1[index]**2
        vec2_l += v2[index]**2
    vec2_l = math.sqrt(vec2_l)
    vec1_l = math.sqrt(vec1_l)
    a = skalar/(vec1_l * vec2_l)
    b = math.acos(a)
    return b

a = [1,2,3]
b = [-1,3,5]
print(math.degrees(function(a,b)))
