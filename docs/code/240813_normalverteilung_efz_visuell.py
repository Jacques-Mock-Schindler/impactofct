# %%

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

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

start = [i for i in range(0,30,3)]
efzs = []

# %%

for s in start:
    data = efz.iloc[:,s:s+3]
    efzs.append(data)
    
efzs.append(efz.iloc[:,-1:])


# %%
bins = [0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25]

# %%

def histogramme(dataframe, count, title=None):
    plt.figure(figsize=(15, 5))

    for i, fach in enumerate(dataframe.columns):
        plt.subplot(1, 3, i + 1)
        ax = sns.histplot(dataframe[fach],
                        bins=bins, 
                        stat='count',
                        kde=False)
        # Normalverteilungskurve
        mu, std = norm.fit(dataframe[fach].dropna())
        xmin, xmax = ax.get_xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p * 80, 
                color='black',
                lw=1,
                linestyle='--')
        
        n = len(dataframe[fach].dropna())
        
        plt.title(f'{fach}\n'
                r'$n =$' + f' {n}, ' +
                r'$\mu =$' + f' {mu:.2f}, ' +
                r'$\sigma =$' + f' {std:.2f}')
        plt.xlabel('Noten')
        plt.ylabel('Absolute Häufigkeit')  # Y-Achse geändert
        ax.set_ylim(0, 75)
        
    if title:
        plt.suptitle(title, 
                     fontsize = 16)

    plt.tight_layout()
    plt.savefig(f'../graphics/test/normalverteilung_efz{count}.png',
                dpi=300)
    plt.show()

# %%

count = 0
for efz in efzs:
    histogramme(efz, count,
                'Histogramme und Normalverteilung der Noten des EFZ')
    count += 1

# %%
