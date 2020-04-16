from selenium import webdriver
import csv, sqlite3, pandas
import time

def getISIN(symbolname):
    myconnection = sqlite3.connect("/home/deeplearning/Documents/PythonScripts/MiningDB.sqlite3")
    mycursor = myconnection.cursor()
    sqlquery = ("select ISIN from ISIN where Symbol = '%s'" %symbolname)
    
    mycursor.execute(sqlquery)
    rows = mycursor.fetchall()
    
    for row in rows:
        isin = row[0]
    
    myconnection.commit()
    myconnection.close()
    return isin

symbolname = "ITC"
ISIN = getISIN(symbolname)
webquery = ("https://financials.morningstar.com/ratios/r.html?t=%s&culture=en&platform=sal" %ISIN)
print(webquery)

d = webdriver.Chrome()
d.get(webquery)
time.sleep(2)
d.find_element_by_css_selector('.large_button').click()
time.sleep(2)
d.quit()