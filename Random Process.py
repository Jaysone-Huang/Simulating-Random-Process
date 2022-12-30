import random
import numpy as np
import pandas as pd
pd.set_option('display.expand_frame_repr', False)

trials  = 100000
q = 0.2
heads = 0 #event Y
trials = 10_000
s = 0
mean =  np.zeros((9,9))
secondMoment = np.zeros((9,9))
variance = np.zeros((9,9))
prob = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
# prob = [0.2, 0.4, 0.6, 0.8]
for j , p in enumerate(prob):
    for k, q in enumerate(prob):
        heads =0
        s = 0
        for i in range(trials):
            n = 0 #event N
            temp=0
            while(True):
                outcome = random.random()
                n+=1
                if(outcome<=p):
                    break
                else:
                    continue
            for i in range(n):
                outcome = random.random()
                if(outcome<=q):
                    heads+=1
                    temp+=1
            s = temp**2+s

        mean[j][k]=heads/trials
        secondMoment[j][k] = s/trials
# print("heads:{} (event Y)".format(heads/trials))

for i in range(9):
    for j in range(9):
        variance[i][j] = secondMoment[i][j]-(mean[i][j]**2)
meandf = pd.DataFrame(data=mean.round(3),columns=prob,index=prob)
vardf = pd.DataFrame(data=variance.round(3),columns=prob,index=prob)

print("Mean:")
print(meandf)
print()
print("Variance:")
print(vardf)

