# %%

import pandas as pd
import numpy as np
from math import sqrt

# %%

df = pd.read_csv('../data/noten_efz.csv',
                 sep=';',
                 index_col=0)

# %%

threshod = 20
columns_counts = df.count()
columns_to_drop = columns_counts[columns_counts < threshod].index.to_list()
df.drop(columns=columns_to_drop, inplace=True)

# %%

numbers = df.count()
numbers = numbers.where(numbers >= 20, np.nan)
numbers = pd.Series(numbers.dropna())

# %%

def margin_error(s, n, p=0.5, z=1.96):
    return  z * sqrt(((p * (1-p)) / s) * ((n - s) / (n - 1)))

# %%

moe = []

for n in numbers:
    e = margin_error(n, 400)
    moe.append((n, e))

print(moe)    

# %%

df2 = pd.DataFrame(moe, columns=['n', 'MoE'])

# %%

headers = df.columns.to_list()

df2.index = headers

# %%

df2.to_csv('../data/margin_of_error.csv',
           sep=';')

# %%
