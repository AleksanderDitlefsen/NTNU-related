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

"""
n = 1000000
x_simulert = simX(n)
a = 0

for i in range(len(x_simulert)):
    if x_simulert[i] <= 2:
        a += 1

print(" Sannsynligheten for at X er mindre enn eller lik 2 er ", a/n)
"""
"""
n = 200_000
x_simulert = simX(n)
E = sum(x_simulert)/n
print(f'Tilnermet verdi for E(x) med {n} simuleringer: ', E)



Var = (sum(x_simulert**2) - n*E**2)/(n-1)
print(f'Standartdavviket SD(x) er med {n} simuleringer tilnermet til: ', np.sqrt(Var))

print(np.std(x_simulert, ddof=1))
"""

def simX2(n, alpha):
    results = []
    for i in range(n):
        u = np.random.uniform()
        results.append(np.sqrt(-np.log(1-u)*alpha))
    return np.array(results)

def f(x, alpha):
    return (2*x/alpha)*np.exp(-x**2/alpha)
    
x_verdier = np.linspace(0, 4, 500)

plt.hist(simX2(100000, 1), bins=100, density=True, alpha=0.6, color='g')
plt.plot(x_verdier, f(x_verdier, 1), color='r')
plt.show()



def simY(n):
    res = np.zeros(n)
    
    for i in range(n):
        U = np.zeros(5)
        
        for j in range(5):
            u = np.random.uniform()
            U[j] = u
        
        a = np.array([np.sqrt(-np.log(1-U[0])),np.sqrt(-np.log(1-U[1])), 0, 0, 0])
        
        for k in range(2, 5):
            b = np.sqrt(-np.log(1-U[k])*1.2)
            a[k] = b
            
        a = np.sort(a)
        res[i] = a[2]
    return res

y = simY(10_000)

plt.hist(y, bins=100, density=True, alpha=0.6, color='k')
plt.show()

P_hat = np.mean(y >= 1)
print(f'P(Y >= 1) er omtrent {P_hat}')
print(f'P(Y >= 1 | Y > 0.75) er omtrent {(P_hat/np.mean(y > 0.75)):.5f}')

print(f'Forventningsverdien til Y er omtrent {np.mean(y):.5f}')
print(f'Standardavviket er omtrent {np.std(y, ddof=1):.5f}')