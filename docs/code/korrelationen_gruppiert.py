# %%

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

# %%

df = pd.read_csv('../data/spearman.csv',
                 sep=';',
                 index_col=0)

# %%

gw_drop = ['M', 'RW', 'WR', 'TU', 'IDAF']

# %%

gw = df.drop(gw_drop, axis='columns')

# %%

gw_header = gw.mean().sort_values()
gw_header = gw_header.index.to_list()

# %%

gw_indices = gw.mean(axis=1).sort_values()
gw_indices = gw_indices.index.to_list()

# %%

gw = gw[gw_header]
gw = gw.reindex(gw_indices)

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
ax = sns.heatmap(gw, annot=True, 
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

plt.title(f'Spearmankorrelation Noten Geisteswissenschaften - EFZ ')
plt.ylabel('EFZ Modul Nr.')
plt.xlabel('Geisteswissenschaften')
plt.savefig('../graphics/spearmankorrelationen_heatmap.png',
            format='png',
            dpi=300)
plt.show()

# %%

sw = pd.DataFrame([df['WR'], df['TU']]).T

# %%

sw_indices = sw.mean(axis=1).sort_values()
sw_indices = sw_indices.index.to_list()
sw_header = sw.mean().sort_values()
sw_header = sw_header.index.to_list()

# %%

sw = sw[sw_header]
sw = sw.reindex(sw_indices)

# %%

plt.figure(
    figsize = (7, 10)
)
ax = sns.heatmap(sw, annot=True, 
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

plt.title(f'Spearmankorrelation Noten Sozialwissenschaften - EFZ ')
plt.ylabel('EFZ Modul Nr.')
plt.xlabel('Sozialwissenschaften')
# plt.savefig('../graphics/spearmankorrelationen_heatmap.svg',
#            dpi=600)
plt.show()

# %%

aw = pd.DataFrame([df['M'], df['RW'], df['IDAF']]).T

# %%

aw_indices = aw.mean(axis=1).sort_values()
aw_indices = aw_indices.index.to_list()
aw_header = aw.mean().sort_values()
aw_header = aw_header.index.to_list()

# %%

aw = aw[aw_header]
aw = aw.reindex(aw_indices)

# %%

plt.figure(
    figsize = (7, 10)
)
ax = sns.heatmap(aw, annot=True, 
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

plt.title(f'Spearmankorrelation Noten abstrakte Wissenschaften - EFZ ')
plt.ylabel('EFZ Modul Nr.')
plt.xlabel('abstrakte Wissenschaften')
# plt.savefig('../graphics/spearmankorrelationen_heatmap.svg',
#            dpi=600)
plt.show()

# %%

modulreihenfolge_gw = gw.index.to_list()
modulreihenfolge_sw = sw.index.to_list()
modulreihenfolge_aw = aw.index.to_list()

# %%

print(modulreihenfolge_gw)
print(modulreihenfolge_sw)
print(modulreihenfolge_aw)

# %%

module = pd.DataFrame(list(zip(modulreihenfolge_gw,
                               modulreihenfolge_sw,
                               modulreihenfolge_aw)),
                      columns=['GW', 'SW', 'AW'])
# %%

mask = ['100', '118', '122',
        '153', '226', '226a',
        '226b', '242', '306',
        '326', '335', '403',
        '411', '431']

# %%

gruppen = module.replace(mask, 1)

# %%

unmask = ['103', '104', '114', '117',
          '120', '123', '133', '150',
          '151', '152', '183', '184',
          '214', '254', '304', '305',
          '404', '426']

# %%

gruppen = gruppen.replace(unmask, 0)

# %%

module = module.astype('string')

# %%

colors = ['#E0E0E0', 'mediumspringgreen']
cmap = sns.color_palette(colors)

# %%

plt.figure(
    figsize = (7, 10)
)

sns.heatmap(gruppen, annot=module.values, fmt='', cmap=cmap, cbar=False, yticklabels=False)

plt.xlabel('Fächergruppen')
plt.title('Verschiebung der CT-Module nach Fächergruppen')

plt.savefig('../graphics/verschiebung.png',
            format='png',
            dpi=300)
plt.show()
# %%

module.dtypes

# %%
