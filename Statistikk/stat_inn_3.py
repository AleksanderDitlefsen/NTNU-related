import numpy as np
import matplotlib.pyplot as plt
import math

#Oppgave 4

def sim_Y(n, forv, sd, a, b):
    verdier = np.zeros(n)

    for i in range(n):
        X = np.random.normal(forv, sd)
        Y = a*X+b
        verdier[i] = Y

    var = a**2*sd**2
    my = a*forv+b

    x_verdier = np.linspace(-10, 15, 1000)
    Y = (1/(np.sqrt(2*var*np.pi)))*np.exp((-1/2)*((x_verdier - my)**2/var))
    plt.plot(x_verdier, Y, color = 'r')

    
    return verdier



plt.hist(sim_Y(100_000, 1, 2, 2, 0.5), 100, density = True, alpha = 0.7, color = 'g')
plt.show()



#STACK

sannsynlighet = 0

for i in range(4):
    sannsynlighet += math.comb(26, i)*(0.2**i)*(0.8**(26-i))

print(1 - sannsynlighet)


