import sys
import datetime
from collections import defaultdict

def read_date(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d")

def calc_week(start_date, date):
    return (read_date(date) - read_date(start_date)).days//7
    
def group_ts(ts):
    results = defaultdict(list)
    start_date = ts[0]
    for date in ts:
        results[calc_week(start_date, date)].append(date)
    return list(results.values())
	
def main(argv):
	group_ts(argv)

if(__name__ = "__main__"):
	main(sys.argv)