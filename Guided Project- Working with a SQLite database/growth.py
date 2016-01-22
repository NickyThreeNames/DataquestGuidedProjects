import pandas as pd
import sqlite3
import math
conn = sqlite3.connect('factbook.db')

a = pd.read_sql_query('SELECT * FROM facts;', con = conn )
a = a.dropna(axis = 0)
a = a[(a['area_land'] > 0) & (a['population'] > 0)]

def pop_grow(x):
    return x['population'] * math.e ** ((x['population_growth']/100) *35)
    
a['pop_2050'] = a.apply(lambda row: pop_grow(row), axis = 1)
b = a.sort(['pop_2050'], ascending = [False])
b = b['name'].iloc[0:9]
print(b)