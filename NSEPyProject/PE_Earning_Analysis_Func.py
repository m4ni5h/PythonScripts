# https://nsepy.readthedocs.io/en/latest/

from nsepy import get_history
from nsepy import get_index_pe_history
from datetime import date
import calendar
import pandas as pd
from pandas import Series, DataFrame

# =(K3-K2)/K2*100
# =(K3-K2)
STARTYEAR = 2011
ENDYEAR = 2020


def indexhistoryyear(indexsymbol, year):
    quarter = [3, 6, 9, 12]
    index_history = pd.DataFrame()
    for n in quarter:
        index_month_history = get_history(symbol=indexsymbol, start=date(year, n, 1),
                                          end=date(year, n, calendar.monthrange(year, n)[1]), index=True)
        index_history = index_history.append(index_month_history.iloc[[-1]])
    return index_history


# indexhistoryyear("NIFTY AUTO", 2019)

def indexhistory(indexsymbol):
    indexhistyear = pd.DataFrame()
    years = range(STARTYEAR, ENDYEAR)
    for year in years:
        indexhistyear = indexhistyear.append(indexhistoryyear(indexsymbol, year))
    indexhistyear = indexhistyear.append(
        get_history(symbol=indexsymbol, start=date(2020, 3, 31), end=date(2020, 3, 31), index=True))
    return indexhistyear


def PEhistoryyear(indexsymbol, year):
    quarter = [3, 6, 9, 12]
    PE_history = pd.DataFrame()
    for n in quarter:
        PE_month_history = get_index_pe_history(symbol=indexsymbol, start=date(year, n, 1),
                                                end=date(year, n, calendar.monthrange(year, n)[1]))
        PE_history = PE_history.append(PE_month_history.iloc[[-1]])
    return PE_history


# PEhistoryyear("NIFTY ENERGY", 2009)

def PEhistory(indexsymbol):
    PEhistyear = pd.DataFrame()
    years = range(STARTYEAR, ENDYEAR)
    for year in years:
        PEhistyear = PEhistyear.append(PEhistoryyear(indexsymbol, year))
    PEhistyear = PEhistyear.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2020, 3, 31), end=date(2020, 3, 31)))
    return PEhistyear


# PEhistory("NIFTY AUTO")

def oldindexhistory(indexsymbol):
    index_history = get_history(symbol=indexsymbol, start=date(2009, 3, 31), end=date(2009, 3, 31), index=True)
    index_history = index_history.append(
        get_history(symbol=indexsymbol, start=date(2010, 3, 31), end=date(2010, 3, 31), index=True))
    index_history = index_history.append(
        get_history(symbol=indexsymbol, start=date(2011, 3, 31), end=date(2011, 3, 31), index=True))
    index_history = index_history.append(
        get_history(symbol=indexsymbol, start=date(2012, 3, 30), end=date(2012, 3, 30), index=True))
    index_history = index_history.append(
        get_history(symbol=indexsymbol, start=date(2013, 3, 28), end=date(2013, 3, 28), index=True))
    index_history = index_history.append(
        get_history(symbol=indexsymbol, start=date(2014, 3, 31), end=date(2014, 3, 31), index=True))
    index_history = index_history.append(
        get_history(symbol=indexsymbol, start=date(2015, 3, 31), end=date(2015, 3, 31), index=True))
    index_history = index_history.append(
        get_history(symbol=indexsymbol, start=date(2016, 3, 31), end=date(2016, 3, 31), index=True))
    index_history = index_history.append(
        get_history(symbol=indexsymbol, start=date(2017, 3, 31), end=date(2017, 3, 31), index=True))
    index_history = index_history.append(
        get_history(symbol=indexsymbol, start=date(2018, 3, 28), end=date(2018, 3, 28), index=True))
    index_history = index_history.append(
        get_history(symbol=indexsymbol, start=date(2019, 3, 29), end=date(2019, 3, 29), index=True))
    index_history = index_history.append(
        get_history(symbol=indexsymbol, start=date(2020, 3, 31), end=date(2020, 3, 31), index=True))
    print(index_history)
    return index_history


def oldPEhistory(indexsymbol):
    pe_history = get_index_pe_history(symbol=indexsymbol, start=date(2009, 3, 31), end=date(2009, 3, 31))
    pe_history = pe_history.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2010, 3, 31), end=date(2010, 3, 31)))
    pe_history = pe_history.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2011, 3, 31), end=date(2011, 3, 31)))
    pe_history = pe_history.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2012, 3, 30), end=date(2012, 3, 30)))
    pe_history = pe_history.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2013, 3, 28), end=date(2013, 3, 28)))
    pe_history = pe_history.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2014, 3, 31), end=date(2014, 3, 31)))
    pe_history = pe_history.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2015, 3, 31), end=date(2015, 3, 31)))
    pe_history = pe_history.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2016, 3, 31), end=date(2016, 3, 31)))
    pe_history = pe_history.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2017, 3, 31), end=date(2017, 3, 31)))
    pe_history = pe_history.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2018, 3, 28), end=date(2018, 3, 28)))
    pe_history = pe_history.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2019, 3, 29), end=date(2019, 3, 29)))
    pe_history = pe_history.append(
        get_index_pe_history(symbol=indexsymbol, start=date(2020, 3, 31), end=date(2020, 3, 31)))
    print(pe_history)
    return pe_history


def earninganalysis(indexsymbol):
    pe_history = PEhistory(indexsymbol)
    index_history = indexhistory(indexsymbol)
    pe_analysis = pd.merge(pe_history, index_history, on='Date')
    earnings = (pe_analysis['Close'] / pe_analysis['P/E']).rename("Earnings")
    earnings = pd.DataFrame(earnings)
    pe_analysis = pd.merge(pe_analysis, earnings, on='Date')
    csvfile = indexsymbol + "_PEAnalysis.csv"
    pe_analysis.to_csv(csvfile)


# earninganalysis("NIFTY INFRASTRUCTURE")
# , "NIFTY ENERGY" 2011,
# "NIFTY FINANCIAL SERVICES", "NIFTY FMCG", "NIFTY METAL", "NIFTY PHARMA", "NIFTY INFRASTRUCTURE"
Indices = ["NIFTY 50", "NIFTY AUTO", "NIFTY BANK", "NIFTY IT", "NIFTY REALTY", "NIFTY COMMODITIES",
           "NIFTY ENERGY",
           # "NIFTY FINANCIAL SERVICES",
           "NIFTY FMCG", "NIFTY METAL", "NIFTY PHARMA"
           # , "NIFTY INFRASTRUCTURE"
           ]
for nseindex in Indices:
    print(nseindex)
    earninganalysis(nseindex)
    print("Done")
