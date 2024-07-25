# %%

import pandas as pd
from scipy.stats import shapiro
from scipy.stats import kstest
from scipy.stats import normaltest
from scipy.stats import spearmanr

# %%

bm = pd.read_csv('../data/noten_bm.csv', sep=';', index_col=0)
efz = pd.read_csv('../data/noten_efz.csv', sep=';', index_col=0)

# %%

threshod = 20
columns_counts = efz.count()
columns_to_drop = columns_counts[columns_counts < threshod].index.to_list()
efz = efz.drop(columns=columns_to_drop)

# %%

headers = list(bm)
indices = list(efz)

# %%

bm_verteilung = pd.DataFrame(index=headers, columns=['shapiro', 'kolmogorov', 'K2'])

# %%

for header in headers:
    resultat = normaltest(bm[header], nan_policy='omit')
    bm_verteilung.loc[header, 'K2'] = resultat.pvalue
    stat, p = shapiro(bm[header], nan_policy='omit')
    bm_verteilung.loc[header, 'shapiro'] = p
    stat, p = kstest(bm[header], 'norm', nan_policy='omit')
    bm_verteilung.loc[header, 'kolmogorov'] = p

# %%

bm_verteilung.to_csv('../data/normalverteilung_bm_zahlen.csv', sep=';')

# %%

efz_verteilung = pd.DataFrame(index=indices, columns=['shapiro', 'kolmogorov', 'K2'])

# %%

for index in indices:
    resultat = normaltest(efz[index], nan_policy='omit')
    efz_verteilung.loc[index, 'K2'] = resultat.pvalue
    stat, p = shapiro(efz[index], nan_policy='omit')
    efz_verteilung.loc[index, 'shapiro'] = p
    stat, p = kstest(efz[index], 'norm', nan_policy='omit')
    efz_verteilung.loc[index, 'kolmogorov'] = p
    
# %%

efz_verteilung.to_csv('../data/normalverteilung_efz_zahlen.csv', sep=';')

# %%
