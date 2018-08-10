# Dealing with outliers
# Reference: StatisticsMachineLearning Sec.5.11

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assume a random variable follows the normal distribution exclude
# data outside 3 standard-deviations: Probability that a sample lies
# within 1-std: 68.27. Probability that a sample lies within 3-std: 99.73

ds = pd.Series(np.random.normal(loc=175,size=20,scale=10))
ds[:1] += 500   # Add one outliers

ds_outlier_mean = ds.copy()
ds_outlier = ds_outlier_mean[(ds-ds.mean()).abs() > 3 * ds.std()]
print(ds_outlier)

# Based on non-parametric statistics: use the median
# Median absolute deviation(MAD), based on the median, is a robust
# non-parametric statistics.
mad = 1.4826 * np.median(np.abs(ds-ds.median()))
ds_outlier_mad = ds.copy()

ds_outlier_mad[((ds-ds.median()).abs()>3*mad)] = ds.median()
print(ds_outlier_mad.median(),ds_outlier_mad.mean())

# Density plot
import seaborn as sns
g = sns.PairGrid(ds)

print('The End.')

