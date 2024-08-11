# %%

import pandas as pd
import numpy as np
from math import sqrt

# %%

df = pd.read_csv('../data/noten_efz.csv',
                 sep=';',
                 index_col=0)

# %%

numbers = df.count()
numbers = numbers.where(numbers >= 20, np.nan)
numbers = pd.Series(numbers.dropna())
numbers.sort_values(inplace=True)
numbers = numbers.unique().tolist()

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
