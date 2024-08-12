# %%

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

# %%

bms = pd.read_csv('../data/noten_bm.csv',
                 sep=';',
                 index_col=0)

# %%

def create_histogramms_grid(dataframe):
    # Vorbereitung für die Einteilung in halbe Noten und Aufbereitung
    # der Datenspalten
    bins = [0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25]
    bin_centers = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
    
    # Erstelle eine 3x3 Figur
    fig, axs = plt.subplots(3, 3, figsize=(15, 15))
    fig.suptitle('Histogramme und Normalverteilungen der Noten der BMS', fontsize=16)
    
    # Berechne das globale Maximum für die y-Achse
    max_count = 0
    for column in dataframe.columns:
        hist, _ = np.histogram(dataframe[column].dropna(), bins=bins)
        max_count = max(max_count, np.max(hist))
    
    for idx, column in enumerate(dataframe.columns):
        row = idx // 3
        col = idx % 3
        ax = axs[row, col]
        
        # Histogramm plotten
        n, bins, patches = ax.hist(dataframe[column].dropna(),
                                   bins=bins, alpha=0.7,
                                   edgecolor='black')
        
        # Grösse der Stichprobe
        size = len(dataframe[column].dropna())
        
        # Normalverteilungskurve berechnen
        mu, std = norm.fit(dataframe[column].dropna())
        xmin, xmax = ax.get_xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        
        # Skaliere die Normalverteilungskurve, um sie an die absoluten Häufigkeiten anzupassen
        scaling_factor = size * (bins[1] - bins[0])
        scaled_p = p * scaling_factor
        
        # Normalverteilungskurve plotten
        ax.plot(x, scaled_p, 'k', 
                linewidth=1, linestyle='--',
                label='Normalverteilung')
        ax.set_title(f'{column}\n' 
                     + r' $n=$'      + f'{size},'
                     + r' $\mu=$'    + f'{mu:.2f},' 
                     + r' $\sigma=$' + f'{std:.2f}')
        
        # Beschriftungen und Darstellung
        ax.set_xlabel('Noten')
        ax.set_ylabel('Absolute Häufigkeit')
        ax.set_xticks(bin_centers)
        ax.grid(axis='y')
        #ax.legend()
        
        # Setze die y-Achse auf das globale Maximum
        ax.set_ylim(0, max_count * 1.1)  # 10% Puffer nach oben
    
    plt.tight_layout()
    plt.savefig('../graphics/normalverteilung_bm_absolut.png',
                dpi=300)
    plt.show()

# %%

create_histogramms_grid(bms)

# %%
