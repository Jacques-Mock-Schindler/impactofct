# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%

df = pd.read_csv('../data/noten_efz.csv',
                 sep=';',
                 index_col=0)

# %%

df['HS 14'] = df[['100', '117', '403', '431']].mean(axis=1)
df['FS 15'] = df[['104', '114', '123', '404']].mean(axis=1)
df['HS 15'] = df[['153', '226a', '411']].mean(axis=1)
df['FS 16'] = df[['226b', '120', '133', '214', '326']].mean(axis=1)
df['HS 16'] = df[['151', '183', '242', '426']].mean(axis=1)
df['FS 17'] = df[['150', '152', '254', '306']].mean(axis=1)

# %%

selected_columns = ['HS 14',
                    'FS 15',
                    'HS 15',
                    'FS 16',
                    'HS 16',
                    'FS 17',]

semester = df[selected_columns].copy()

# %%

plt.figure(
    figsize=(12, 6)
)

ax = sns.boxplot(data=semester, 
            color='skyblue',
            medianprops={'color': 'red'})

plt.title('Semsternoten')
plt.xlabel('Semester')
plt.ylabel('Noten')
plt.tight_layout()
plt.savefig('../graphics/semesternoten_efz.svg',
            dpi=600)
plt.show()

# %%
