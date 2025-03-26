#To stimulate the transport progress of illness.
#1--Infected  0--Susceptible  2--Resistant
import numpy as np
import matplotlib.pyplot as plt
# definite the initial variables
size = 100  
beta = 0.3  
gamma = 0.05  
steps = 100
#make the first infection point
population = np.zeros((size, size), dtype=int)
outbreak = (np.random.randint(0, size), np.random.randint(0, size))
population[outbreak] = 1
for t in range(steps):
    new_population = population.copy()
    for i in range(size):
        for j in range(size):
            if population[i, j] == 1: 
                for x in range(max(i-1, 0), min(i+2, size)):
                    for y in range(max(j-1, 0), min(j+2, size)):
                        if population[x, y] == 0: 
                            new_population[x, y] = np.random.choice([0, 1], p=[1-beta, beta])
                new_population[i, j] = np.random.choice([1, 2], p=[1-gamma, gamma])

    population = new_population.copy()
plt.figure(figsize=(6, 6), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("SIR 2D Simulation")
plt.colorbar(label="0: S, 1: I, 2: R")
plt.show()
                
        

