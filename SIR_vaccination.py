import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

# Create the variables and the relative values to start the modal
N=10000
beta=0.3
gamma=0.05

#create the list to store the values of the variables
I_list=[1]
plt.figure(figsize=(10, 5))
#carry the stimulation
for J in np.arange(0.00, 1.10, 0.10):# adjust the population of vaccinated people
    I = 1
    R=int(10000*J)#the number of people who have been vaccinated 
    S=9999-R
    S=max(S,0)
    for i in range(1000):
        new_recovered=np.random.choice(range(2),I, p=[1-gamma,gamma]) #for every infected person, we calculate the probability of recovering
        sum_new_recovered=sum(new_recovered)
        R=R+sum_new_recovered
        infected_rate=beta*I/N
        increase_infected=np.random.choice(range(2),S,p=[1-infected_rate,infected_rate])#for every susceptible person, we calculate the probability of being infected
        sum_increase_infected=sum(increase_infected)
        I =I+ sum_increase_infected - sum_new_recovered
        S=S-sum_increase_infected
        I_list.append(I)
    plt.plot(I_list, label = f'{J:.0%}', color = cm.viridis(J))
    I_list=[1]
plt.xlabel("Time Steps")
plt.ylabel("Population")
plt.title("SIR Model Simulation")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('SIRpicture with vaccination',type='png')