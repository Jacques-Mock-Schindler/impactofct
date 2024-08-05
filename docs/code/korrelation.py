# %%

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from scipy.stats import shapiro
from scipy.stats import kstest
from scipy.stats import normaltest
from scipy.stats import spearmanr

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
    
pearson = pd.DataFrame(index=indices, columns=headers)

# %%

for header in headers:
    for index in indices:
        tmp = pd.concat([bm[header], efz[index]], axis="columns")
        tmp.dropna(axis="index", inplace=True)
        r = tmp[index].corr(tmp[header])
        pearson.loc[index, header] = r
        
# %%

pearson.to_csv('../data/korrelationen.csv', sep=';')

# %%

pearson = pearson.select_dtypes(include=['object']).astype(float)

# %%

mittelwerte = pearson.median()
mittelwerte.sort_values(inplace=True)
sortierreihenfolge = mittelwerte.index.to_list()

# %%

querwerte = pearson.median(axis=1)
querwerte.sort_values(inplace=True)
sortierreihenfolge_quer = querwerte.index.to_list()

# %%

pearson = pearson[sortierreihenfolge]
pearson = pearson.reindex(sortierreihenfolge_quer)

# %%

colors = ['#808080', '#A0A0A0', '#C0C0C0', '#E0E0E0',  # Greys
          '#F0F0F0',  # Very light grey (almost white) for the center
          '#E0FFE0', '#C0FFC0', '#80FF80', '#40FF40', '#00FF00']  # Greens
n_bins = 256  # Number of color gradations
grey_to_green = LinearSegmentedColormap.from_list('custom_grey_green', colors, N=n_bins)

# %%

plt.figure(
    figsize = (7, 10)
)
ax = sns.heatmap(pearson, annot=True, 
            cmap=grey_to_green, 
            vmin=-.2, vmax=.6, center=0.3)
for col in range(1, 9):
    ax.axvline(x=col, color='black', linewidth=.5)
plt.title(f'Pearson\'s r Noten BM - EFZ ')
plt.ylabel('EFZ Modul Nr.')
plt.xlabel('BM Fächer')
    
yticklabels = ax.get_yticklabels()
for label in yticklabels:
    if label.get_text() in ['100', '118', '122',
                            '153', '226', '226a',
                            '226b', '242', '306',
                            '326', '335', '403',
                            '411', '431']:
        label.set_color('red')
    else:
        label.set_color('black')
        
plt.savefig('../graphics/korrelationen_heatmap.png',
            format='png',
           dpi=300)
plt.show()

# %%

spearman = pd.DataFrame(index=indices, columns=headers)

# %%

for header in headers:
    for index in indices:
        tmp = pd.concat([bm[header], efz[index]], axis="columns")
        tmp.dropna(axis="index", inplace=True)
        tmpx = tmp[header]
        tmpy = tmp[index]
        cor, p = spearmanr(tmpx, tmpy)
        spearman.loc[index, header] = cor
        

# %%

spearman = spearman.select_dtypes(include=['object']).astype(float)

# %%

spearman.to_csv('../data/spearman.csv', sep=';')

# %%

mittelwerte = spearman.median()
mittelwerte.sort_values(inplace=True)
sortierreihenfolge = mittelwerte.index.to_list()
spearman = spearman[sortierreihenfolge]

# %%

querwerte = spearman.median(axis=1)
querwerte.sort_values(inplace=True)
sortierreihenfolge_quer = querwerte.index.to_list()
spearman = spearman.reindex(sortierreihenfolge_quer)

# %%

plt.figure(
    figsize = (7, 10)
)
ax = sns.heatmap(spearman, annot=True, 
            cmap=grey_to_green, 
            vmin=-.2, vmax=.6, center=0.3)
for col in range(1, 9):
    ax.axvline(x=col, color='black', linewidth=.5)
    
yticklabels = ax.get_yticklabels()
for label in yticklabels:
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
plt.savefig('../graphics/spearman_heatmap.png',
            format='png',
           dpi=300)
plt.show()

# %%