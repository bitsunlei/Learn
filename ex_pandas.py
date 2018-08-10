import pandas as pd
import numpy as np
import matplotlib as plt


# Create a series
a = pd.Series([1,2,4,np.nan,6,8])
print(a)

# Create a dataframe
col_names = ['name','age','gender','job']
b = pd.DataFrame([['alice',19,'F',"student"],['John',26,"M","student"]],columns=col_names)

user1 = pd.DataFrame([['alice', 19, "F", "student"],
                        ['John', 26, "M", "student"]],
                        columns=col_names)
user2 = pd.DataFrame([['eric', 22, "M", "student"],
                        ['paul', 58, "F", "manager"]],
                        columns=col_names)
user4 = pd.DataFrame(dict(name=['alice','John','paul'],
                          height=[154,149,290]))

# Concatenate dataframe
b = pd.concat([user1,user2])
b = pd.merge(b,user4,on='name')
print(b)

# Copy dataframe
c = b.copy()

# Statistics
c.describe()


print('The End.')
