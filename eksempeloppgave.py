import random
import numpy as np

def TerningKast(n):
    a_sum = 0
    b_sum = 0
    for i in range(n):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        a_sum += a
        b_sum += b
    print(f'Average sum when throwing two dice {n} times: {(a_sum + b_sum) / n}')

TerningKast(1000000)