import csv, sqlite3
import pandas

con = sqlite3.connect("/home/deeplearning/Documents/PythonScripts/MiningDB.sqlite3")
cur = con.cursor()

df = pandas.read_csv("/home/deeplearning/Documents/PythonScripts/MorningStarDataMining/SymbolToISIN.csv")
df.to_sql("ISIN1", con, if_exists='append', index=False)

con.commit()
con.close()