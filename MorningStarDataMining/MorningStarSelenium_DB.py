from selenium import webdriver
import csv, sqlite3, pandas
import time

# Get the ISIN for the symbol passed
# Result from ISIN table in the SQLITE Database, upgrade DB if the symbol is not found
def getISIN(symbolname):
    myconnection = sqlite3.connect("MiningDB.sqlite3")
    mycursor = myconnection.cursor()
    sqlquery = ("select ISIN from ISIN where Symbol = '%s'" %symbolname)
    
    mycursor.execute(sqlquery)
    rows = mycursor.fetchall()
    
    for row in rows:
        isin = row[0]
    
    myconnection.commit()
    myconnection.close()
    return isin

#### MODIFY ONLY THIS PART ######
symbolname = "ITC"
slowspeed = 2
#################################
ISIN = getISIN(symbolname)
webquery = ("https://financials.morningstar.com/ratios/r.html?t=%s&culture=en&platform=sal" %ISIN)

d = webdriver.Chrome()
d.get(webquery)
time.sleep(slowspeed)

# CSV file is downloaded in the default Chrome download folder.
d.find_element_by_css_selector('.large_button').click()
time.sleep(slowspeed)
d.quit()