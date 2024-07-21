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

headers = list(bm)
headers = headers[:8]
indices = list(efz_reduced)

# %%

correlations = pd.DataFrame(index=indices, columns=headers)

# %%

for header in headers:
    for index in indices:
        tmp = pd.concat([bm[header], efz[index]], axis="columns")
        tmp.dropna(axis="index", inplace=True)
        r = tmp[index].corr(tmp[header])
        correlations.loc[index, header] = r
        
# %%
