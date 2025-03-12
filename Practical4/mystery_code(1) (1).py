# What does this piece of code do?
# Answer:	to determine after how many loops the two random variables have the same value.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil 

progress=0 # initialize progress
while progress>=0: # infinite loop
	progress+=1 
	first_n = randint(1,6)
	second_n = randint(1,6)
	if first_n == second_n: # if the two random numbers are the same, print the progress and break the loop
		print(progress)
		break

