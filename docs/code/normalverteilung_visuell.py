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

efz = pd.read_csv('../data/noten_efz.csv',
                  sep=';',
                  index_col=0)

# %%

threshod = 20
columns_counts = efz.count()
columns_to_drop = columns_counts[columns_counts < threshod].index.to_list()
efz.drop(columns=columns_to_drop, inplace=True)

# %%

efz1 = efz.iloc[:,:12]
efz2 = efz.iloc[:,12:24]
efz3 = efz.iloc[:,24:]

# %%

def create_histogramms(dataframe):
    # Vorbereitung für die Einteilung in halbe Noten und Aufbereitung
    # der Datenspalten
    bins = [0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25]
    bin_centers = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
        
    for column in dataframe.columns:
        plt.figure()
        
        # Histogramm plotten
        n, bins, patches = plt.hist(dataframe[column].dropna(),
                                    bins=bins, alpha=0.7,
                                    edgecolor='black', 
                                    density=True)
        
        # Normalverteilungskurve berechnen
        mu, std = norm.fit(dataframe[column].dropna())
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        
        # Normalverteilungskurve plotten
        plt.plot(x, p, 'k', 
                 linewidth=1, linestyle='--',
                 label='Normalverteilung')
        plt.title(f'Histogramm und Normalverteilung für {column}\n'
                  + r' $\mu=$' +f'{mu:.2f}' 
                  + r' $\sigma=$' +f'{std:.2f}')
        
        # Beschriftungen und Darstellung
        plt.xlabel('Noten')
        plt.ylabel('Häufigkeit')
        plt.xticks(bin_centers)
        plt.grid(axis='y')
        plt.legend()
        
        plt.show()
        

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
    max_density = 0
    for column in dataframe.columns:
        hist, _ = np.histogram(dataframe[column].dropna(), bins=bins, density=True)
        max_density = max(max_density, np.max(hist))
    
    for idx, column in enumerate(dataframe.columns):
        row = idx // 3
        col = idx % 3
        ax = axs[row, col]
        
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
        ax.set_title(f'{column}\n' 
                     + r' $n=$'      + f'{size},'
                     + r' $\mu=$'    + f'{mu:.2f},' 
                     + r' $\sigma=$' + f'{std:.2f}')
        
        # Beschriftungen und Darstellung
        ax.set_xlabel('Noten')
        ax.set_ylabel('Häufigkeit')
        ax.set_xticks(bin_centers)
        ax.grid(axis='y')
        #ax.legend()
        
        # Setze die y-Achse auf das globale Maximum
        ax.set_ylim(0, max_density * 1.1)  # 10% Puffer nach oben
    
    plt.tight_layout()
    plt.savefig('../graphics/normalverteilung_bm.png',
                dpi=300)
    plt.show()

# %%

create_histogramms_grid(bms)

# %%

def create_histogramms_grid_efz(dataframe):
    # Vorbereitung für die Einteilung in halbe Noten und Aufbereitung
    # der Datenspalten
    bins = [0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25]
    bin_centers = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
    
    # Berechne die Anzahl der Zeilen basierend auf der Anzahl der Spalten
    num_cols = len(dataframe.columns)
    num_rows = math.ceil(num_cols / 3)
    
    # Erstelle eine Figur mit der berechneten Anzahl von Zeilen und 3 Spalten
    fig, axs = plt.subplots(num_rows, 3, figsize=(15, 5*num_rows + 2))
    
    fig.suptitle('Histogramme und Normalverteilungen der Noten der Berufsausbildung (Teil 3)',
                 fontsize=16, y=1)
    
    # Berechne das globale Maximum für die y-Achse
    max_density = 0
    for column in dataframe.columns:
        hist, _ = np.histogram(dataframe[column].dropna(), bins=bins, density=True)
        max_density = max(max_density, np.max(hist))

    for idx, column in enumerate(dataframe.columns):
        row = idx // 3
        col = idx % 3
        
        # Überprüfe, ob axs ein 2D-Array ist (mehr als eine Zeile)
        if num_rows > 1:
            ax = axs[row, col]
        else:
            ax = axs[col]
        
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
        ax.set_ylim(0, max_density * 1.1)  # 10% Puffer nach oben
    
    # Entferne leere Subplots
    for idx in range(num_cols, num_rows * 3):
        row = idx // 3
        col = idx % 3
        if num_rows > 1:
            fig.delaxes(axs[row, col])
        else:
            fig.delaxes(axs[col])
    
    plt.tight_layout()
    plt.savefig('../graphics/normalverteilung_efz_3.png',
                dpi=300)
    plt.show()
# %%

create_histogramms_grid_efz(efz3)

# %%
