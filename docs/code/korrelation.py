# %%

import pandas as pd

# %%

bm = pd.read_csv('../data/noten_bm.csv', sep=';', index_col=0)
efz = pd.read_csv('../data/noten_efz.csv', sep=';', index_col=0)

# %%

threshod = 20
columns_counts = efz.count()
columns_to_drop = columns_counts[columns_counts < threshod].index.to_list()
efz_reduced = efz.drop(columns=columns_to_drop)

# %%
