# Dealing with Elementary Statistics
# Reference: StatisticsMachineLearning Sec.7.1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate 2 random samples: x- N(1.78,0.1) and y- N(1.66,0.1), size 10
x = pd.Series(np.random.normal(1.76,size=10,scale=0.1))
y = pd.Series(np.random.normal(1.66,size=10,scale=0.1))

print('Variances of Series x and y')
print(np.var(x),np.std(x))
print(np.var(y),np.std(y))
print(np.cov(x,y))

# Normal distribution
import scipy.stats as scs
mu  = 0;
sig = 2;    # sig = sqrt(variance)

x = np.linspace(mu-3*(sig**2),mu+3*(sig**2),100)
plt.plot(x,scs.norm.pdf(x,mu,sig))
# plt.show()

print('The End.')

