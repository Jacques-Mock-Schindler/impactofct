# %%

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

# %%

efz = pd.read_csv('../data/noten_efz.csv',
                  sep=';',
                  index_col=0)


# %%

threshod = 20
columns_counts = efz.count()
columns_to_drop = columns_counts[columns_counts < threshod].index.to_list()
efz.drop(columns=columns_to_drop, inplace=True)

# %%

efzs = []

start = [i for i in range(0,30,3)]

for s in start:
    data = efz.iloc[:,s:s+3]
    efzs.append(data)
    
efzs.append(efz.iloc[:,-1:])
    
# %%

def create_histogramms_grid_efz(dataframe, counter):
    # Vorbereitung für die Einteilung in halbe Noten und Aufbereitung
    # der Datenspalten
    bins = [0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25]
    bin_centers = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
    
    # Erstelle eine Figur mit 1 Zeile und 3 Spalten
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    
    fig.suptitle('Histogramme und Normalverteilungen der Noten des EFZ',
                 fontsize=16, y=1.05)
    
    # Berechne das globale Maximum für die y-Achse
    max_density = 0
    for column in dataframe.columns:
        hist, _ = np.histogram(dataframe[column].dropna(), bins=bins, density=True)
        max_density = max(max_density, np.max(hist))

    for idx, column in enumerate(dataframe.columns):
        ax = axs[idx]
        
        # Histogramm plotten
        n, bins, patches = ax.hist(dataframe[column].dropna(),
                                   bins=bins, alpha=0.7,
                                   edgecolor='black', 
                                   density=True)
        
        # Grösse der Stichprobe
        size = len(dataframe[column].dropna())
        
        # Normalverteilungskurve berechnen
        mu, std = norm.fit(dataframe[column].dropna())
        xmin, xmax = ax.get_xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        
        # Normalverteilungskurve plotten
        ax.plot(x, p, 'k', 
                linewidth=1, linestyle='--',
                label='Normalverteilung')
        ax.set_title(f'Modul {column}\n' 
                     + r' $n$ ' + f'{size},'
                     + r' $\mu=$' + f'{mu:.2f},' 
                     + r' $\sigma=$' + f'{std:.2f}')
        
        # Beschriftungen und Darstellung
        ax.set_xlabel('Noten')
        ax.set_ylabel('Häufigkeit')
        ax.set_xticks(bin_centers)
        ax.grid(axis='y')
        # ax.legend()
        
        # Setze die y-Achse auf das globale Maximum
        ax.set_ylim(0, 1.1)  # 10% Puffer nach oben
    
    plt.tight_layout()
    plt.savefig(f'../graphics/test/normalverteilung_efz{counter}.png',
                dpi=300, bbox_inches='tight')
    plt.show()
    

# %%

counter = 0
for efz in efzs:
    create_histogramms_grid_efz(efz, counter)
    counter += 1

