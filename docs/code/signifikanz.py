# %%

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import scipy.stats as stats
from scipy.stats import shapiro
from scipy.stats import kstest
from scipy.stats import normaltest
from scipy.stats import spearmanr
import numpy as np

# %%

bm = pd.read_csv('../data/noten_bm.csv',
                 sep=';',
                 index_col=0)
efz = pd.read_csv('../data/noten_efz.csv',
                  sep=';',
                  index_col=0)


# %%

threshod = 20
columns_counts = efz.count()
columns_to_drop = columns_counts[columns_counts < threshod].index.to_list()
efz_reduced = efz.drop(columns=columns_to_drop)

# %%

headers = list(bm)
indices = list(efz_reduced)
    
# %%
    
pearson_r = pd.DataFrame(index=indices, columns=headers)
pearson_p = pd.DataFrame(index=indices, columns=headers)
spearman_r = pd.DataFrame(index=indices, columns=headers)
spearman_p = pd.DataFrame(index=indices, columns=headers)

# %%

for header in headers:
    for i in indices:
        tmp = pd.concat([bm[header], efz_reduced[i]], 
                        axis="columns")
        tmp.dropna(axis="index", inplace=True)
        if len(tmp) >= 2:
            r, p = stats.pearsonr(tmp[header], tmp[i])
            rs, ps = stats.spearmanr(tmp[header], tmp[i])
            pearson_r.loc[header, i] = r
            pearson_p.loc[header, i] = p
            spearman_r.loc[header, i] = rs
            spearman_p.loc[header, i] = ps
        else:
            pearson_r.loc[header, i] = 99
            pearson_p.loc[header, i] = 99
            spearman_r.loc[header, i] = 99
            spearman_p.loc[header, i] = 99
        

# %%

pearson_p = pearson_p.iloc[31:,9:]
pearson_p.to_csv('../data/pearson_signifikanztest.csv',
                 sep=';')

# %%

result = pearson_p[pearson_p >= 0.05]

# %%

result_index_head = [(row, col) for row in result.index for col in result.columns if result.at[row, col] >= 0.05]

# %%

spearman_p = spearman_p.iloc[31:,9:]

# %%

spearman_p.to_csv('../data/spearman_signifikanz.csv',
                  sep=';')

# %%

result_spearman = spearman_p[spearman_p >= 0.05]
result_index_head_spearman = [(row, col) for row in result.index for col in result.columns if result.at[row, col] >= 0.05]

# %%

len(result_index_head_spearman)

# %%
