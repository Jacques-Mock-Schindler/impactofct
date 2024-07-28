# %%

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

# %%

bm = pd.read_csv('../data/noten_bm.csv', sep=';', index_col=0)

# %%

plt.figure(
    figsize=(12, 6)
)

sns.boxplot(data=bm, color='skyblue')
plt.title('Notenverteilung in der BMS')
plt.xlabel('Fächer')
plt.ylabel('Noten')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%

main_color = 'springgreen'
last_color = 'mediumaquamarine'

colors = [main_color] * (len(bm.columns) - 1) + [last_color]

plt.figure(
    figsize=(12, 6)
)

sns.boxplot(data=bm, palette=colors)
plt.title('Notenverteilung in der BMS')
plt.xlabel('Fächer')
plt.ylabel('Noten')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../graphics/boxplots_bm.svg', dpi=600)
plt.show()

# %%

efz = pd.read_csv('../data/noten_efz.csv', sep=';', index_col=0)

# %%


plt.figure(
    figsize=(12, 6)
)

sns.boxplot(data=efz, color='skyblue')
plt.title('Notenverteilung im EFZ')
plt.xlabel('Module')
plt.ylabel('Noten')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# %%
