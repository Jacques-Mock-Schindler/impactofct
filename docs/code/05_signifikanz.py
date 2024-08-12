# %%

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import scipy.stats as stats
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
efz.drop(columns=columns_to_drop, inplace=True)

# %%

headers = list(bm)
indices = list(efz)
    
# %%
    
pearson_r = pd.DataFrame(index=indices, columns=headers)
pearson_p = pd.DataFrame(index=indices, columns=headers)
spearman_r = pd.DataFrame(index=indices, columns=headers)
spearman_p = pd.DataFrame(index=indices, columns=headers)

# %%

for header in headers:
    for i in indices:
        tmp = pd.concat([bm[header], efz[i]], 
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
result.T

# %%

result_index_head = [(row, col) for row in result.index for col in result.columns if result.at[row, col] >= 0.05]

# %%

spearman_p = spearman_p.iloc[31:,9:]

# %%

spearman_p.to_csv('../data/spearman_signifikanz.csv',
                  sep=';')

# %%

result_spearman = spearman_p[spearman_p >= 0.05]
result_spearman.T
cells_to_highlight = [(row, col) for row in result.index for col in result.columns if result.at[row, col] >= 0.05]

# %%

spearman = pd.DataFrame(index=indices, columns=headers)

# %%


colors = ['#808080', '#A0A0A0', '#C0C0C0', '#E0E0E0',  # Greys
          '#F0F0F0',  # Very light grey (almost white) for the center
          '#E0FFE0', '#C0FFC0', '#80FF80', '#40FF40', '#00FF00']  # Greens
n_bins = 256  # Number of color gradations
grey_to_green = LinearSegmentedColormap.from_list('custom_grey_green', colors, N=n_bins)


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
        
for cell in cells_to_highlight:
    col, row = cell
    col_idx = spearman.columns.get_loc(col)
    row_idx = spearman.index.get_loc(row)
    ax.add_line(plt.Line2D([col_idx, col_idx+1], [row_idx, row_idx+1], color='gray', lw=1))

plt.title(r"Spearman's $\rho$ Noten BM - EFZ")
plt.ylabel('EFZ Modul Nr.')
plt.xlabel('BM Fächer')
plt.savefig('../graphics/spearman_heatmap.png',
            format='png',
           dpi=300)
plt.show()
# %%

31* 9

# %%
