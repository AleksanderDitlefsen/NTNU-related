"Oppgave 1: a) Her må man summere sammen f(0), f(1) og f(2), som er 0.05 + 0.1 + 0.25 = 0.40."

import numpy as np
import matplotlib.pyplot as plt


def simX(n):
    f_x = np.array([0.05,0.10,0.25,0.40,0.15,0.05])

    F_x = [np.sum(f_x[:i]) for i in range(1,7)]
        # verdimengde
    x = np.arange(6)
        # for lagring av realisasjoner
    x_sim = np.zeros(n)
    for i in range(n):      # vi simulerer hver og en x for seg
        u = np.random.uniform()        # en realisasjon fra U(0,1)
        if(u < F_x[0]):        # hvis u er mindre enn den laveste
        # verdien i F_x vil
        # vi at realisasjonen skal være 0
            x_sim[i] = x[0]
        elif(u <= F_x[1]): # hvis u er mindre enn den nest
        # laveste verdien (men større enn laveste)
        # vil vi at x skal bli 1
            x_sim[i] = x[1]
        elif(u <= F_x[2]):
            x_sim[i] = x[2]
        elif(u <= F_x[3]):
            x_sim[i] = x[3]
        elif(u <= F_x[4]):
            x_sim[i] = x[4]
        elif(u > F_x[4]):
            x_sim[i] = x[5]
    return x_sim

n = 1000000
x_simulert = simX(n)
a = 0

for i in range(len(x_simulert)):
    if x_simulert[i] <= 2:
        a += 1

print(" Sannsynligheten for at X er mindre enn eller lik 2 er ", a/n)