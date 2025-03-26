import numpy as np
import matplotlib.pyplot as plt
import random

# Create the variables and the relative values to start the modal
N=10000
I=1
S=9999
R=0
beta=0.3
gamma=0.05
t=0

#create the list to store the values of the variables
S_list=[9999]
I_list=[1]
R_list=[0]

# Create the loop to calculate the values of the variables
for i in range(1000):
    new_recovered=np.random.choice(range(2),I, p=[1-gamma,gamma]) #for every infected person, we calculate the probability of recovering
    sum_new_recovered=sum(new_recovered)
    R=R+sum_new_recovered
    R_list.append(R)
    infected_rate=beta*I/N
    increase_infected=np.random.choice(range(2),S,p=[1-infected_rate,infected_rate])#for every susceptible person, we calculate the probability of being infected
    sum_increase_infected=sum(increase_infected)
    I =I+ sum_increase_infected - sum_new_recovered
    S=S-sum_increase_infected
    I_list.append(I)
    S_list.append(S)
# draw the line chart to show the chengement during the experiment
plt.figure(figsize=(10, 5))
plt.plot(S_list, label='Susceptible', color='blue')
plt.plot(I_list, label='Infected', color='red')
plt.plot(R_list, label='Recovered', color='green')
plt.xlabel("Time Steps")
plt.ylabel("Population")
plt.title("SIR Model Simulation")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('STRpicture',type='png')