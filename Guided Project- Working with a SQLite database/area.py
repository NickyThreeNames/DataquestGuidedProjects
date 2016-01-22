import pandas as pd
import sqlite3

conn = sqlite3.connect('factbook.db')

a = pd.read_sql_query('SELECT SUM(area_land), SUM(area_water) FROM facts WHERE area_land != "";', con = conn)

print(a['SUM(area_land)'] / a['SUM(area_water)'])