# Hypothesis Test
# Reference: StatisticsMachineLearning Sec.7.3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# The one-sample t-test is used to determine whether a sample
# comes from a population with a specific mean. For example,
# you want to test if the average height of a population is 1.75m

# 1. Model the data:
# Assume that height is normally distributed: X-N(mu,sig)
mu0 = 1.75
sig = 1
# x = pd.Series(np.random.normal(mu,scale=sig,size=10))
x= [ 1.83, 1.83, 1.73, 1.82, 1.83, 1.73, 1.99, 1.85, 1.68, 1.87]

# 2. Fit: estimate the model parameters
# x_bar and x_s are the estimators of mu and sigma, respectively.
x_bar = np.mean(x)
x_s = np.std(x,ddof=1)

# 3. Test: In testing the Null hypothesis that the population mean
# is equal to a specific value mu0 = 175, one uses the statisitic:
# t- (x_bar-mu0)/(x_s/sqrt(n))
n = len(x)

tobs = (x_bar-mu0)/(x_s/np.sqrt(n))
print('Hypothesis Testing tobs')
print(tobs)

# 4. The math: p-value is the probability to observe a value t more
# extreme than the observed one tobs under the Null hypothesis
# H0: P(t>tobs|H0)
import scipy.stats as stats
tvalues = np.linspace(-10,10,100)
plt.plot(tvalues,stats.t.pdf(tvalues,n-1),'b-',label="T(n-1)")
upper_tval_tvalues = tvalues[tvalues>tobs]
plt.fill_between(upper_tval_tvalues,0,stats.t.pdf(upper_tval_tvalues,n-1),
                 alpha=0.8,label="p-value")
plt.legend()
plt.show()

n = 50
x = np.random.normal(size=n)
y = x*2 #+ np.random.normal(size=n)

cor,pval = stats.pearsonr(x,y)
print(cor,pval)


print('The End.')

