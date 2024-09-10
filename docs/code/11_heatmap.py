# %%

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from scipy.stats import spearmanr
# %%

df = pd.read_csv('../data/spearman.csv',
                 sep=';',
                 index_col=0)

df = df.T

# %%

colors = ['#808080', '#A0A0A0', '#C0C0C0', '#E0E0E0',  # Greys
          '#F0F0F0',  # Very light grey (almost white) for the center
          '#E0FFE0', '#C0FFC0', '#80FF80', '#40FF40', '#00FF00']  # Greens
n_bins = 256  # Number of color gradations
grey_to_green = LinearSegmentedColormap.from_list('custom_grey_green', colors, N=n_bins)

# %%

mittelwerte = df.median()
mittelwerte.sort_values(inplace=True)
sortierreihenfolge = mittelwerte.index.to_list()
df = df[sortierreihenfolge]

# %%

querwerte = df.median(axis=1)
querwerte.sort_values(inplace=True)
sortierreihenfolge_quer = querwerte.index.to_list()
df = df.reindex(sortierreihenfolge_quer)

# %%

plt.figure(
    figsize = (15, 7)
)
ax = sns.heatmap(df, annot=False, 
            cmap=grey_to_green, 
            vmin=-.2, vmax=.6, center=0.3)
#for col in range(1, 9):
#    ax.axvline(x=col, color='black', linewidth=.5)
    
xticklabels = ax.get_xticklabels()
for label in xticklabels:
    if label.get_text() in ['100', '118', '122',
                            '153', '226', '226a',
                            '226b', '242', '306',
                            '326', '335', '403',
                            '411', '431']:
        label.set_color('red')
    else:
        label.set_color('black')

plt.title(r"Spearman's $\rho$ Noten BM - EFZ")
plt.ylabel('EFZ Modul Nr.')
plt.xlabel('BM Fächer')
plt.savefig('../praesentation/illustrationen/spearman_heatmap.svg',
            format='svg',
            dpi=300)
plt.show()


# %%
