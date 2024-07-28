# %%

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%

bm = pd.read_csv('../data/noten_bm.csv', sep=';', index_col=0)

# %%

plt.figure(
    figsize=(12, 6)
)
sns.boxplot(data=bm)
plt.title('Notenverteilung in der BMS')
plt.xlabel('Fächer')
plt.ylabel('Noten')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
