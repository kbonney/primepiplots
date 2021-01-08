import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

#
def pi(n):
    n = np.floor(n).astype(int)
    if isinstance(n,(list,np.ndarray)):
        out = []
        for cur_num in n:
            out.append(sp.primepi(cur_num))
            
        return out
    else:
        out=0
        for x in range(1,n):
            if sp.isprime(x):
                out+=1
        return out
def digappx(n):
    n = np.floor(n).astype(int)
    if isinstance(n,(list,np.ndarray)):
        out = []
        for cur_num in n:
            out.append(cur_num / (2*len(str(cur_num))))
        return out
    else:
        out=n / len(str(n))
        return out
    
# Data for plotting
t = np.arange(5, 100000, 0.1)
s = pi(t) #/ np.floor(t).astype(int)
v = 1 / np.log(t)
w = digappx(t)
u = t / np.log(t)

fig, ax = plt.subplots()
ax.plot(t,s, color='green')
ax.plot(t,u, color='orange')
ax.plot(t,w, color='blue')
ax.set(xlabel='x', ylabel='pi(x)/x',
       title='Primeywimey')
ax.grid()

fig.savefig("test.png")
plt.show()
#print(w)
