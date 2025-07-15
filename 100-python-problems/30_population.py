'''	
The current population of a town is 10000.
The population of the town is increasing at the rate of 10% per year.
You have to write a program to find out the population at the end of each of the last 10 years. 
For eg current population is 10000 so the output should be like this:
10th year - 10000
9th year - 9000
8th year - 8100 and so on
 '''
import math
def population():

    cur_population = 10000

    for i in range(10,-1,-1):
        if i == 10:
            print("10th year population -",cur_population)
        else:

            pop = cur_population - (0.10 * cur_population)
            print(f"{i}th year population -",math.floor(pop))
            cur_population =math.floor(pop)

population()