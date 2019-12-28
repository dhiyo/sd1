print("hello")#https://github.com/ResearchCodesHub/SGA/blob/master/SGA%20-%20SimpleFunction.py
#R.Lahoz - Beltra
import math
import random
import numpy as np
import matplotlib.pyplot as plt
N=50                 # Population size
Genome=4             # Genome length
generation_max= 650  # Maximum of generations - iterations

#########################################################
# Define your problem in this section. For instance:    #
#                                                       #
# Let f(x)=abs(x-5/2+sin(x)) be a function that takes   #
# values in the range 0<=x<=15. Within this range f(x)  #
# has a maximum value at x=11 (binary is equal to 1011) #
#########################################################
GenomeLength=4
popSize=4
chromosome = np.empty([popSize, GenomeLength],dtype=np.int)
import numpy as np


###########################
# Population Initiaztion
##########################
def Init_population():
    for j in range(1,popSize):
        print("pop")
        print(j)
        for i in range(1,GenomeLength):
            all=np.random.randint(0,100)
            all=all/100
            #print(all)
            if (all<=0.5):
                chromosome[i,j]=0
            else:
                chromosome[i,j]=1
        print(chromosome)



#########################################################
# SHOW POPULATION                                       #
#########################################################
def Show_population():
    for i in range(1,popSize):
        for j in range(1,genomeLength):
            print(chromosome[i,j],end="")
        print()
#########################################################
# FITNESS EVALUATION                                    #
#########################################################

fitness=[]
tot_fitness=0
vv=[4,5,6,7 ]
for i in range(1,popSize):
    x=0
    print(i)
    for j in range(1,GenomeLength):
           # translate from binary to decimal value
           print(j)
           x=x+chromosome[i,j]
           x=x*pow(2,GenomeLength-j-1)
          # replaces the value of x in the function f(x)
           y= np.fabs((x-5)/(2+np.sin(x)))
           # the fitness value is calculated below:
           # (Note that in this example is multiplied
           # by a scale value, e.g. 100)
           #print(y)
           a=y
    vv[i]=a
    print(a)
    print("hello")
    print(vv[i])
    tot_fitness=tot_fitness+vv[i]
    avg_fit=tot_fitness/popSize
print(tot_fitness)
print(avg_fit)

print(vv)
kk=[1,2,3,4]
sum_sqr=0
for i in range(1,popSize):
    print(kk[i])
    print(avg_fit)
    kk[i]=vv[i]-(avg_fit)
    kk[i]=pow(kk[i],2)
    print(kk[i])
    sum_sqr=sum_sqr+kk[i]
    var=sum_sqr/popSize
    print(var)

print("Population size = ", popSize - 1)
print("mean fitness = ",avg_fit)
print("variance = ",var," Std. deviation = ",math.sqrt(var))
#print("fitness max = ",best_chrom[generation])
#print("fitness sum = ",fitness_total)

####Wheel Selection###

