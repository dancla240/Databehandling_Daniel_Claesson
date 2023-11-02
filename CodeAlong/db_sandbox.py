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

#%%
my_list = ['name','email','job_title']

print(my_list[0])

for item in range(len(my_list)):
    my_list[item] = my_list[item].title()
    
print(my_list)

my_list[0] = 'NamE'

print(my_list)

#%%
import pandas as pd

employees = pd.read_json("C:/Users/danie/Documents/Github/Databehandling_Daniel_Claesson/Data/employees.json")

employees

my_cols = employees.columns

my_cols_update = []

for item in my_cols:
    print(item)
    my_cols_update.append(item.title())

print(my_cols_update)

employees.columns = my_cols_update

employees
#%%
title = "job_title"

if "_" in title:
    title.replace("_", " ")

print(title)

"job_title".replace("_", " ")