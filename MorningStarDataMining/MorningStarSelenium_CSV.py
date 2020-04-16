from selenium import webdriver
import csv, sqlite3, pandas
import time
import os
#cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

# Get the ISIN for the symbol passed
# Result from CSV from https://www1.nseindia.com/corporates/corporateHome.html?id=equity, update CSV if Symbol not found
def getISIN(symbolname):
    ISINTable = pandas.read_csv("SymbolToISIN.csv")
    print(ISINTable)
    isin = ISINTable.loc[ISINTable["Symbol"] == "TCS"]["ISIN"].item()
    print(isin)
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