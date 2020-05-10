from nsepy import get_history
from datetime import date


def indexhistory(indexsymbol):
    nifty_index = get_history(symbol=indexsymbol, start=date(2009,3,31), end=date(2009,3,31), index=True)
    nifty_index = nifty_index.append(get_history(symbol=indexsymbol, start=date(2010,3,31), end=date(2010,3,31), index=True))
    nifty_index = nifty_index.append(get_history(symbol=indexsymbol, start=date(2011,3,31), end=date(2011,3,31), index=True))
    nifty_index = nifty_index.append(get_history(symbol=indexsymbol, start=date(2012,3,30), end=date(2012,3,30), index=True))
    nifty_index = nifty_index.append(get_history(symbol=indexsymbol, start=date(2013,3,28), end=date(2013,3,28), index=True))
    nifty_index = nifty_index.append(get_history(symbol=indexsymbol, start=date(2014,3,31), end=date(2014,3,31), index=True))
    nifty_index = nifty_index.append(get_history(symbol=indexsymbol, start=date(2015,3,31), end=date(2015,3,31), index=True))
    nifty_index = nifty_index.append(get_history(symbol=indexsymbol, start=date(2016,3,31), end=date(2016,3,31), index=True))
    nifty_index = nifty_index.append(get_history(symbol=indexsymbol, start=date(2017,3,31), end=date(2017,3,31), index=True))
    nifty_index = nifty_index.append(get_history(symbol=indexsymbol, start=date(2018,3,28), end=date(2018,3,28), index=True))
    nifty_index = nifty_index.append(get_history(symbol=indexsymbol, start=date(2019,3,29), end=date(2019,3,29), index=True))
    nifty_index = nifty_index.append(get_history(symbol=indexsymbol, start=date(2020,3,31), end=date(2020,3,31), index=True))
    print(nifty_index)
    return nifty_index

indexhistory("NIFTY").to_csv('IndexHistory.csv')
