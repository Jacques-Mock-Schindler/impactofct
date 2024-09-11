# %%

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import pandas as pd

# %%

plt.rcParams['svg.fonttype'] = 'none'

df = pd.read_csv('../data/spearman.csv', 
                 sep=';',
                 index_col=0)

# %%

mask = {'100': 1, '118': 1, '122': 1,
        '153': 1, '226': 1, '226a': 1,
        '226b': 1, '242': 1, '306': 1,
        '326': 1, '335': 1, '403': 1,
        '411': 1, '431': 1,}
df['kategorie'] = df.index.map(mask)
df['kategorie'] = df['kategorie'].fillna(0)

gw = df.iloc[:,:3]
k = df.iloc[:,-1:]
gw['mean'] = gw.mean(axis='columns')
gw = pd.concat([gw, k], axis='columns')
gw.sort_values(by='mean', inplace=True)

sw = df.iloc[:,5:8]
sw['mean'] = sw.mean(axis='columns')
sw = pd.concat([sw, k], axis='columns')
sw.sort_values(by='mean', inplace=True)

values_sw = sw['mean'].to_list()
categories_sw = sw['kategorie'].to_list()

values = gw['mean'].to_list()
categories = gw['kategorie'].to_list()

aw = df.loc[:,['M', 'RW', 'IDAF']]
aw['mean'] = aw.mean(axis='columns')
aw = pd.concat([aw, k], axis='columns')
aw.sort_values(by='mean', inplace=True)

values_aw = aw['mean'].to_list()
categories_aw = aw['kategorie'].to_list()

# %%

def create_barcode(values, categories, figsize=(10, 2)):
    # Erstelle eine neue Figur mit transparentem Hintergrund
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_alpha(0)  # Make figure background transparent
    ax.patch.set_alpha(0)   # Make axes background transparent
    
    # Setze die y-Achse auf einen festen Bereich
    ax.set_ylim(0, 1)
    
    # Entferne die Achsen
    ax.axis('off')
    
    # Erstelle eine Farbpalette
    colors = ['#FFFFFF', '#F8FFF8', 'limegreen']  # Weiß, sehr helles Grün, Grün
    positions = [0.0, 0.3, 1.0]
    
    # Erstelle die Farbpalette
    cmap = LinearSegmentedColormap.from_list("custom_green", list(zip(positions, colors)))
    
    max_value = max(values)
    
    # Initialisiere die x-Position
    x = 0
    
    # Iteriere über die Werte und Kategorien
    for i, (value, category) in enumerate(zip(values, categories)):
        # Setze die Farbe basierend auf der Kategorie
        if category == 0:
            color = 'gray'
        else:
            # Normalisiere den Wert und wähle die entsprechende Farbe
            normalized_value = value / max_value
            color = cmap(normalized_value)
        
        # Zeichne den Balken
        ax.add_patch(plt.Rectangle((x, 0), value, 1, facecolor=color, edgecolor='blue'))
        
        # Aktualisiere die x-Position für den nächsten Balken
        if i < len(values) - 1:
            x += value + (values[i+1] - value) / 2
    
    # Setze die x-Achse auf den Bereich der Daten
    ax.set_xlim(0, x)
    
    return fig

# %%
# Erstelle und speichere die Barcodes
fig = create_barcode(values_aw, categories_aw)
plt.title('M, RW sowie IDAF')
plt.savefig('../illustrationen/aw_transparent.svg',
            dpi=300,
            format = 'svg',
            transparent=True,
            bbox_inches='tight')
plt.close(fig)  # Close the figure to free up memory

fig = create_barcode(values, categories)
plt.title('D, F, E')
plt.savefig('../illustrationen/gw_transparent.svg',
            dpi=300,
            format = 'svg',
            transparent=True,
            bbox_inches='tight')
plt.close(fig)  # Close the figure to free up memory

fig = create_barcode(values_sw, categories_sw)
plt.title('WR, GuP, TU')
plt.savefig('../illustrationen/sw_transparent.svg',
            dpi=300,
            format = 'svg',
            transparent=True,
            bbox_inches='tight')
plt.close(fig)  # Close the figure to free up memory

# %%
