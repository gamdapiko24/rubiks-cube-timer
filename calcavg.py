# calcavg.py

import math

def mean(items):
    filtered = [i for i in items if isinstance(i, (int, float))]
    return float(round(sum(filtered)/len(filtered),2))

def aox(x,times):
    recent = times[-x:]
    if recent.count('DNF') >= 2:
        return 'DNF'
    
    numeric_times = []
    for t in recent:
        try:
            numeric_times.append(float(t))
        except ValueError:
            pass
    if len(numeric_times) < x:
        return 'N/A'
    numeric_times.remove(min(numeric_times))
    numeric_times.remove(max(numeric_times))