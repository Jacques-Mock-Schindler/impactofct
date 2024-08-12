# %%

import pandas as pd
import matplotlib.pyplot as plt
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

modulreihenfolge_gw = gw.index.to_list()
modulreihenfolge_sw = sw.index.to_list()
modulreihenfolge_aw = aw.index.to_list()

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

sns.heatmap(gruppen, annot=module.values,
            fmt='', cmap=cmap, cbar=False,
            yticklabels=False)

plt.xlabel('Fächergruppen')
plt.title('Verschiebung der CT-Module nach Fächergruppen')

plt.savefig('../graphics/verschiebung.png',
            format='png',
            dpi=300)
plt.show()

# %%

