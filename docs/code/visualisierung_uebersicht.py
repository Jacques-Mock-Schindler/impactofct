# %%

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

# %%

bm = pd.read_csv('../data/noten_bm.csv', sep=';', index_col=0)

# %%

plt.figure(
    figsize=(12, 6)
)

sns.boxplot(data=bm, color='skyblue')
plt.title('Notenverteilung in der BMS')
plt.xlabel('Fächer')
plt.ylabel('Noten')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%

main_color = 'springgreen'
last_color = 'mediumaquamarine'

colors = [main_color] * (len(bm.columns) - 1) + [last_color]

plt.figure(
    figsize=(12, 6)
)

ax = sns.boxplot(data=bm, 
            medianprops={'color': 'red', 'linewidth': 2},
            palette=colors)

# Anpassungen für die IDAF-Box
boxes = ax.patches                     # mache die Boxen einzeln ansprechbar
last_box = boxes[-1]                   # wähle die letze Box aus
last_box.set_linestyle('--')           # linestyle dashed
r, g, b, a = last_box.get_facecolor()  # Lese die Farbattribute aus
last_box.set_facecolor((r, g, b, 0.5)) # Setze die Transparenz auf 50%
whiskers = ax.lines[-6:-4] # die letzen 6 Linien gehören zum letzen Plot...
caps = ax.lines[-4:-2]
median = ax.lines[-2]

for whisker in whiskers:
    whisker.set_linestyle('--')
for cap in caps:
    cap.set_linestyle('--')
median.set_linestyle('--')

plt.title('Notenverteilung in der BMS')
plt.xlabel('Fächer')
plt.ylabel('Noten')
plt.tight_layout()
plt.savefig('../graphics/boxplots_bm.svg', dpi=600)
plt.show()

# %%

efz = pd.read_csv('../data/noten_efz.csv', sep=';', index_col=0)

# %%


plt.figure(
    figsize=(12, 6)
)

sns.boxplot(data=efz, color='skyblue')
plt.title('Notenverteilung im EFZ')
plt.xlabel('Module')
plt.ylabel('Noten')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# %%
