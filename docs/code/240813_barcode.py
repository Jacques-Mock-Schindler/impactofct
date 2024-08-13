# %%

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %%

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

# %%

gw = df.iloc[:,:3]
k = df.iloc[:,-1:]
gw = pd.concat([gw, k], axis='columns')


# %%

gw['mean'] = gw.mean(axis='columns')


# %%

def create_barcode(values, categories, figsize=(10, 2)):
    # Erstelle eine neue Figur
    fig, ax = plt.subplots(figsize=figsize)
    
    # Setze die y-Achse auf einen festen Bereich
    ax.set_ylim(0, 1)
    
    # Entferne die Achsen
    ax.axis('off')
    
    # Initialisiere die x-Position
    x = 0
    
    # Iteriere über die Werte und Kategorien
    for i, (value, category) in enumerate(zip(values, categories)):
        # Setze die Farbe basierend auf der Kategorie
        color = 'black' if category == 0 else 'red'
        
        # Zeichne den Balken
        ax.add_patch(plt.Rectangle((x, 0), value, 1, facecolor=color, edgecolor='none'))
        
        # Aktualisiere die x-Position für den nächsten Balken
        if i < len(values) - 1:
            x += value + (values[i+1] - value) / 2
    
    # Setze die x-Achse auf den Bereich der Daten
    ax.set_xlim(0, x)
    
    return fig

# %%

# Beispieldaten
values = np.random.rand(20)
categories = np.random.randint(0, 2, 20)

# %%

# Erstelle den Strichcode
fig = create_barcode(values, categories)

# Zeige die Figur an
plt.show()
# %%
