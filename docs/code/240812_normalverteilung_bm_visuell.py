# %%

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# %%

bms = pd.read_csv('../data/noten_bm.csv',
                 sep=';',
                 index_col=0)

# %%

bms1 = bms.iloc[:,:3]
bms2 = bms.iloc[:,3:6]
bms3 = bms.iloc[:,6:9]

bmss = [bms1, bms2, bms3]

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
        mu, std = np.mean(dataframe[fach]), np.std(dataframe[fach])
        x = np.linspace(1, 6, 100)
        p = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / std) ** 2)
        plt.plot(x, p * 80, 
                color='black',
                lw=1,
                linestyle='--')
        plt.title(f'{fach}\n'
                r'$n =$' + f' {len(dataframe[fach])}, ' +
                r'$\mu =$' + f' {mu:.2f}, ' +
                r'$\sigma =$' + f' {std:.2f}')
        plt.xlabel('Noten')
        plt.ylabel('Absolute Häufigkeit')  # Y-Achse geändert
        ax.set_ylim(0, 75)
        
    if title:
        plt.suptitle(title, 
                     fontsize = 16)

    plt.tight_layout()
    plt.savefig(f'../graphics/test/normalverteilung_bms{count}.png',
                dpi=300)
    plt.show()

# %%

count = 1
for bms in bmss:
    histogramme(bms, count)
    count += 1

# %%
