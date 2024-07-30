# %%

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%

bm  = pd.read_csv('../data/noten_bm.csv',
                 sep=';',
                 index_col=0)
efz = pd.read_csv('../data/noten_efz.csv',
                  sep=';',
                  index_col=0)

# %%

bm['mittelwert_bm']   = bm.mean(axis='columns')
efz['mittelwert_efz'] = efz.mean(axis='columns')

# %%

combi = pd.concat([bm['mittelwert_bm'], efz['mittelwert_efz']],
                  axis='columns',
                  join='outer')

# %%

plt.figure(
    figsize=(12, 6)
)

sns.regplot(data=combi,
                x='mittelwert_bm',
                y='mittelwert_efz',
                line_kws = {'color': 'red'})

plt.title('Korrelation BMS - EFZ')
plt.xlabel('Noten BMS')
plt.ylabel('Noten EFZ')
plt.show()

# %%
