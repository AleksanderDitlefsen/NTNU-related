import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

#Oppgave 1 b)

def sim_A(n):
    
    resultat = np.zeros(n)
    
    for i in range(n):
        X = np.random.normal(150, 5)
        Y = np.random.normal(200, 7)
        Phi = np.random.normal(0.9, 0.05)

        A = 0.5*X*Y*np.sin(Phi)

        resultat[i] = A
    
    forv = np.sum(resultat)/n

    a = 0
    for k in resultat:
        a += (k - forv)**2

    var = a/n
    SD = np.sqrt(var)


    return forv, var, SD, resultat

a = sim_A(10_000)
b = a[0]
c = a[1]
d = a[2]

x_verdier = np.linspace(8_000, 15_000, 1000)
y_verdier = (1 / (d * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_verdier - b) / d)**2)

plt.hist(a[3], 50, density = True, alpha = 0.6, color = "g")
plt.plot(x_verdier, y_verdier, color = "r")
plt.xlabel("Areal i kvadratmeter")
plt.ylabel("Sannsynlighet")
plt.show()

print(f"Med 10 000 simuleringer blir SD approksimert til {d:.3f}, varians til {c:.3f} og forventningsverdi til {b:.3f}.")




#Oppgave 3 c)

def sim_X_and_Y(r, n, m, l):

    estimated_lambda = np.zeros(r)

    alpha = (2*n)/(m + 2*n)
    beta = (2*m)/(m + 2*n)

    for j in range(r):

        Y_verdier = np.zeros(m)
        X_verdier = np.zeros(n)

        for i in range(n):
            a = np.random.poisson(l)
            X_verdier[i] = a
        
        for k in range(m):
            b = np.random.poisson(l/2)
            Y_verdier[k] = b

        estimated_lambda[j] = alpha * np.sum(X_verdier)/n + beta * np.sum(Y_verdier)/m

    plt.hist(estimated_lambda, 25, density = True, alpha = 0.6, color = 'g')
    sm.qqplot(estimated_lambda)
    plt.show()

sim_X_and_Y(1000, 42, 35, 12)

# Hvis man myser litt med øynene så vil man være tilbøyelig til å kalle denne fordelingen for en normalfordeling,
# men det er ikke noe jeg sier med veldig høy sikkehet

# Når man så plott i et qqplot, så ser man at punktene våre helt klart er normalfordelt.
# Vi får en linje med punkter som ligger meget tett opp på diagonalen --> normalfordelt

# Den teoretiske begrunnelsen for at estimated_lambda er tilnærmet normalfordelt er at
# poissonfordelingen er en fordeling som kan sammenlignes med normsalfordelingen, og uttrykket for
# lambda_tilde består av en sum av gjennomsnittet av disse fordelingene. Det er kjent at den nye stokastiske variabelen
# vil være tilnærmet normalfordelt --> Sentralgrenseteoremet




# Oppgave 5

# Den enkleste måten å sjekke om dataene er normalfordelte er å plotte dataen inn i et histogram og se om
# den karakteristiske normalkruven dukker opp, men i dette tilfellet er det så lite data at dette blir uoptimalt.
# Det beste for små datasett er QQ-plott, og det er nettop det vi skal gjøre.

x = np.array([-2.5, 0.5, 3.3, 2.6, -0.7, -4.6, 3.3, 0.8, 1.9, -0.5, 1.2, 3.8])    # Data fra tabell
y = np.array([4.1, 7.2, 5.0, 7.9, 5.8, 4.9, 5.0, 5.9, 6.9, 4.8, 6.7, 3.2])


sm.qqplot(x)
plt.title('X-verdier')
sm.qqplot(y)
plt.title('Y-verdier')
plt.tight_layout()
plt.show()