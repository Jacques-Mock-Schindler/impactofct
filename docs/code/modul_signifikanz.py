# %%

import pandas as pd
from math import sqrt

# %%

def margin_error(s, n, p=0.5, z=1.96):
    return  z * sqrt(((p * (1-p)) / s) * ((n - s) / (n - 1)))

# %%

margin_error(167, 400)

# %%
