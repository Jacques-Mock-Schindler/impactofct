# %%

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%

plt.rcParams['svg.fonttype'] = 'none'

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

fig, ax = plt.subplots(figsize=(15, 7))
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)
ax.set_facecolor('none')

sns.regplot(data=combi,
                x='mittelwert_bm',
                y='mittelwert_efz',
                line_kws = {'color': 'red'})

plt.title('Korrelation BMS - EFZ')
plt.xlabel('Noten BMS')
plt.ylabel('Noten EFZ')
plt.savefig('../praesentation/illustrationen/mittlere_korrelation.svg',
            format='svg',
            dpi=300)
plt.show()

# %%

fig, ax = plt.subplots(figsize=(15, 7))
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)
ax.set_facecolor('none')

ax = sns.boxplot(data=combi,
            color='skyblue',
            width=0.5,
            medianprops={'color': 'red'})

plt.title('Verteilung der Notendurchschnitte BMS und EFZ')
plt.ylabel('Noten')
plt.xlabel('Durchschnitte')
ax.set_xticklabels(['BMS', 'EFZ'])
plt.tight_layout()
plt.savefig('../graphics/verteilung_durchschnitte.png',
            format='png',
            dpi=300)
plt.show()

# %%