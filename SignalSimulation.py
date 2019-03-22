#The intention of this code is to simuulate a signal from a production line sensor with random noise

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

length = 1000+1
fact = "null"
y = np.linspace(0,length,length)


rsig = rand.randint(0,10,length)
#rsig = y/100+rsig
rsig = np.sin(y*100)+rsig


x = np.array([])

#Assuming that 0 means system is off, and 3 is considered an optimal level of vibration

for i in range(0,length):
    sig = rsig.item(i)
    if sig == 0:
        #print("Machine is off")
        fact = 0
        x = np.append(x,fact)
    if sig == 3:
        #print("Machine is at optimal state")
        fact = 0
        x = np.append(x,fact)
    elif sig > 8:
        #print("Machine is near failure")
        fact = 5
        x = np.append(x,fact)
    elif sig > 5:
        #print("Machine is operating poorly")
        fact = 4
        x = np.append(x,fact)
    elif sig > 3:
        #print("Machine is operating above optimal")
        fact = 3
        x = np.append(x,fact)


active = np.size(x)
#print(active)
rsig = rsig[:active]

unique_elements, counts_elements = np.unique(x,return_counts=True)
print(np.asarray((unique_elements, counts_elements)))
print(unique_elements)
print(counts_elements)
"""
#print(np.size(rsig))
plt.plot(rsig)
plt.plot(x,"x")

plt.show()
"""
