from nsepy import get_history
from nsepy import get_index_pe_history
from datetime import date
import pandas as pd
from pandas import Series, DataFrame

def indexhistory(indexsymbol):
    index_history = get_history(symbol=indexsymbol, start=date(2009,3,31), end=date(2009,3,31), index=True)
    index_history = index_history.append(get_history(symbol=indexsymbol, start=date(2010,3,31), end=date(2010,3,31), index=True))
    index_history = index_history.append(get_history(symbol=indexsymbol, start=date(2011,3,31), end=date(2011,3,31), index=True))
    index_history = index_history.append(get_history(symbol=indexsymbol, start=date(2012,3,30), end=date(2012,3,30), index=True))
    index_history = index_history.append(get_history(symbol=indexsymbol, start=date(2013,3,28), end=date(2013,3,28), index=True))
    index_history = index_history.append(get_history(symbol=indexsymbol, start=date(2014,3,31), end=date(2014,3,31), index=True))
    index_history = index_history.append(get_history(symbol=indexsymbol, start=date(2015,3,31), end=date(2015,3,31), index=True))
    index_history = index_history.append(get_history(symbol=indexsymbol, start=date(2016,3,31), end=date(2016,3,31), index=True))
    index_history = index_history.append(get_history(symbol=indexsymbol, start=date(2017,3,31), end=date(2017,3,31), index=True))
    index_history = index_history.append(get_history(symbol=indexsymbol, start=date(2018,3,28), end=date(2018,3,28), index=True))
    index_history = index_history.append(get_history(symbol=indexsymbol, start=date(2019,3,29), end=date(2019,3,29), index=True))
    index_history = index_history.append(get_history(symbol=indexsymbol, start=date(2020,3,31), end=date(2020,3,31), index=True))
    print(index_history)
    return index_history

def PEhistory(indexsymbol):
    pe_history = get_index_pe_history(symbol=indexsymbol, start=date(2009,3,31), end=date(2009,3,31))
    pe_history = pe_history.append(get_index_pe_history(symbol=indexsymbol, start=date(2010,3,31), end=date(2010,3,31)))
    pe_history = pe_history.append(get_index_pe_history(symbol=indexsymbol, start=date(2011,3,31), end=date(2011,3,31)))
    pe_history = pe_history.append(get_index_pe_history(symbol=indexsymbol, start=date(2012,3,30), end=date(2012,3,30)))
    pe_history = pe_history.append(get_index_pe_history(symbol=indexsymbol, start=date(2013,3,28), end=date(2013,3,28)))
    pe_history = pe_history.append(get_index_pe_history(symbol=indexsymbol, start=date(2014,3,31), end=date(2014,3,31)))
    pe_history = pe_history.append(get_index_pe_history(symbol=indexsymbol, start=date(2015,3,31), end=date(2015,3,31)))
    pe_history = pe_history.append(get_index_pe_history(symbol=indexsymbol, start=date(2016,3,31), end=date(2016,3,31)))
    pe_history = pe_history.append(get_index_pe_history(symbol=indexsymbol, start=date(2017,3,31), end=date(2017,3,31)))
    pe_history = pe_history.append(get_index_pe_history(symbol=indexsymbol, start=date(2018,3,28), end=date(2018,3,28)))
    pe_history = pe_history.append(get_index_pe_history(symbol=indexsymbol, start=date(2019,3,29), end=date(2019,3,29)))
    pe_history = pe_history.append(get_index_pe_history(symbol=indexsymbol, start=date(2020,3,31), end=date(2020,3,31)))
    print(pe_history)
    return pe_history

pe_history = PEhistory("NIFTY ENERGY")
index_history = indexhistory("NIFTY ENERGY")

pe_analysis = pd.merge(pe_history, index_history, on='Date')

earnings = (pe_analysis['Close']/pe_analysis['P/E']).rename("Earnings")
earnings =pd.DataFrame(earnings)

pe_analysis = pd.merge(pe_analysis, earnings, on='Date')

pe_analysis.to_csv("NIFTY ENERGY_peanalysis.csv")