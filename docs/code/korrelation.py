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

bm = pd.read_csv('../data/noten_bm.csv', sep=';', index_col=0)
efz = pd.read_csv('../data/noten_efz.csv', sep=';', index_col=0)

# %%

threshod = 20
columns_counts = efz.count()
columns_to_drop = columns_counts[columns_counts < threshod].index.to_list()
efz_reduced = efz.drop(columns=columns_to_drop)

# %%

headers = list(bm)
#headers = headers[:8]
indices = list(efz_reduced)

# %%

bm_verteilung = pd.DataFrame(index=headers, columns=['shapiro', 'kolmogorov', 'K2'])

# %%

resultat = normaltest(bm['D'])
float(resultat.pvalue)


# %%

for header in headers:
    resultat = normaltest(bm[header])
    normal = 0.05 < float(resultat.pvalue)
    bm_verteilung.loc[header, 'K2'] = normal
    stat, p = shapiro(bm[header])
    normal = 0.05 < float(p)
    bm_verteilung.loc[header, 'shapiro'] = normal
    stat, p = kstest(bm[header], 'norm')
    normal = 0.05 < float(p)
    bm_verteilung.loc[header, 'kolmogorov'] = normal
        

# %%

bm_verteilung.to_csv("../data/normalverteilung_bm.csv", sep=";")
    
    
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

correlations.to_csv('../data/korrelationen.csv', sep=';')

# %%

correlations = correlations.select_dtypes(include=['object']).astype(float)

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
ax = sns.heatmap(correlations, annot=True, 
            cmap=grey_to_green, 
            vmin=-.2, vmax=.6, center=0.3)
for col in range(1, 9):
    ax.axvline(x=col, color='black', linewidth=.5)
plt.title(f'Korrelation Noten BM - EFZ ')
plt.ylabel('EFZ Modul Nr.')
plt.xlabel('BM Fächer')
plt.savefig('../graphics/korrelationen_heatmap.svg',
            dpi=600)
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

spearman.min()

# %%

plt.figure(
    figsize = (7, 10)
)
ax = sns.heatmap(spearman, annot=True, 
            cmap=grey_to_green, 
            vmin=-.2, vmax=.6, center=0.3)
for col in range(1, 9):
    ax.axvline(x=col, color='black', linewidth=.5)
plt.title(f'Spearmankorrelation Noten BM - EFZ ')
plt.ylabel('EFZ Modul Nr.')
plt.xlabel('BM Fächer')
plt.savefig('../graphics/spearmankorrelationen_heatmap.svg',
            dpi=600)
plt.show()


# %%
