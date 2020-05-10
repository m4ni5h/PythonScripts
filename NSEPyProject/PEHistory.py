from nsepy import get_index_pe_history
from datetime import date, datetime, timedelta
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

thisyear = datetime.now().year
thismonth = datetime.now().month
thisday = datetime.now().day
Indices = []
with open("BroadMarketIndices.txt", "rt") as f:
    for line in f:
        if(line[0] != "#"):
            line = line.rstrip('\n')
            Indices.append(line)
i = 1
for broadindex in Indices:
    broadindex = broadindex.upper()
    pe = get_index_pe_history(symbol=broadindex, start=date(thisyear, thismonth-1, 1), end=date(thisyear, thismonth, thisday))
    print(pe)
    pe.to_csv('data/%d_%s.csv'%(i,broadindex))
    i += 1
