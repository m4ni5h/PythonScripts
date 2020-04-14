from nsepy import get_index_pe_history
from datetime import date
import pandas as pd
from pandas import Series, DataFrame


def PEhistory(indexsymbol):
    nifty_pe = get_index_pe_history(symbol=indexsymbol, start=date(2009,3,31), end=date(2009,3,31))
    nifty_pe = nifty_pe.append(get_index_pe_history(symbol=indexsymbol, start=date(2010,3,31), end=date(2010,3,31)))
    nifty_pe = nifty_pe.append(get_index_pe_history(symbol=indexsymbol, start=date(2011,3,31), end=date(2011,3,31)))
    nifty_pe = nifty_pe.append(get_index_pe_history(symbol=indexsymbol, start=date(2012,3,30), end=date(2012,3,30)))
    nifty_pe = nifty_pe.append(get_index_pe_history(symbol=indexsymbol, start=date(2013,3,28), end=date(2013,3,28)))
    nifty_pe = nifty_pe.append(get_index_pe_history(symbol=indexsymbol, start=date(2014,3,31), end=date(2014,3,31)))
    nifty_pe = nifty_pe.append(get_index_pe_history(symbol=indexsymbol, start=date(2015,3,31), end=date(2015,3,31)))
    nifty_pe = nifty_pe.append(get_index_pe_history(symbol=indexsymbol, start=date(2016,3,31), end=date(2016,3,31)))
    nifty_pe = nifty_pe.append(get_index_pe_history(symbol=indexsymbol, start=date(2017,3,31), end=date(2017,3,31)))
    nifty_pe = nifty_pe.append(get_index_pe_history(symbol=indexsymbol, start=date(2018,3,28), end=date(2018,3,28)))
    nifty_pe = nifty_pe.append(get_index_pe_history(symbol=indexsymbol, start=date(2019,3,29), end=date(2019,3,29)))
    nifty_pe = nifty_pe.append(get_index_pe_history(symbol=indexsymbol, start=date(2020,3,31), end=date(2020,3,31)))
    print(nifty_pe)
    return nifty_pe

PEhistory("NIFTY").to_csv('PEHistory.csv')