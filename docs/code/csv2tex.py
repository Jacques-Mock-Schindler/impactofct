# %%

import pandas as pd

# %%

df = pd.read_csv('../data/noten_efz.csv', sep=';')

df.iloc[:,1:] = df.iloc[:,1:].round(1)

# %%

latex_table = df.to_latex(index=False, longtable=True,
                          float_format='%.1f', 
                          caption='Modulnoten Berufsausbildung',
                          label='tbl:noten_efz')

# %%

with open ('noten_efz.tex', 'w') as f:
    f.write(latex_table)
    
# %%
