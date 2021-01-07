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

# Data for plotting
t = np.arange(0.0, 100, 0.1)
s = pi(t) / np.floor(t).astype(int)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='x', ylabel='pi(x)/x',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
