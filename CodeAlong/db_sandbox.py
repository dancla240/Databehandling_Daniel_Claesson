# sandbox for databehandlingskursen:

#%%
# skapar en dataframe fr�n en dict
# printar den
# df.info()
# skapar ett series object av Col_A

import pandas as pd

data = {
        'Col_A':[1,2,3,4,5],
        'Col_B':["a","b","c","d","e"]
        }

my_df = pd.DataFrame(data)

print(my_df)
my_df.info()

my_series = pd.Series(my_df['Col_A'])
print(my_series)
type(my_series)

my_df.describe()

print(my_df['Col_B'])