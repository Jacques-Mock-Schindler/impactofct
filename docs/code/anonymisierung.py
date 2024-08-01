# %%

import pandas as pd
import hashlib

# %%

def hash_column(df, column_name, hash_length=16):
    def short_hash(value):
        return hashlib.sha256(str(value).encode()).hexdigest()[:hash_length]
    
    df[f'{column_name}_hash'] = df[column_name].apply(short_hash)
    return df

# %%

df = pd.read_csv('240720_notenliste_bm.csv', sep=';')

# %%

df.drop('Klasse', axis=1, inplace=True)

# %%

df['names'] = df['Name'] + df['Vorname']

# %%

df = hash_column(df, 'names')

# %%

df.set_index('names_hash', inplace=True)

# %%

df.drop(['Name', 'Vorname', 'names'], axis=1, inplace=True)

# %%

df.to_csv('noten_bm.csv', sep=';')

# %%
