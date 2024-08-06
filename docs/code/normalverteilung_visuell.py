# %%

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


# %%

df = pd.read_csv('../data/noten_bm.csv',
                 sep=';',
                 index_col=0)

# %%

def create_histogramms(dataframe):
    # Vorbereitung für die Einteilung in halbe Noten und Aufbereitung
    # der Datenspalten
    bins = [0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25]
    bin_centers = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
        
    for column in dataframe.columns:
        plt.figure()
        
        # Histogramm plotten
        n, bins, patches = plt.hist(dataframe[column],
                                    bins=bins, alpha=0.7,
                                    edgecolor='black', 
                                    density=True)
        
        # Normalverteilungskurve berechnen
        mu, std = norm.fit(dataframe[column])
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        
        # Normalverteilungskurve plotten
        plt.plot(x, p, 'k', linewidth=2)
        title = f'Histogramm und Normalverteilung für {column}\n$\mu={mu:.2f}$, $\sigma={std:.2f}$'
        
        # Beschriftungen und Darstellung
        plt.title(title)
        plt.xlabel('Noten')
        plt.ylabel('Häufigkeit')
        plt.xticks(bin_centers)
        plt.grid(axis='y')
        
        plt.show()
        

# %%

df.drop('IDAF', axis='columns', inplace=True)

# %%

create_histogramms(df)
# %%
