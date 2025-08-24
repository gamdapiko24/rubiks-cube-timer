# timedictgen.py

import calcavg, json
from pathlib import Path

timedata = {'3x3': {'solve': [],
                    'date': [],
                    'time': [],
                    'scramble': [],
                    'comments': [],
                    'mo3': [],
                    'ao5': [],
                    'ao12': [],
                    'mean': [],
                    }
            }

dperevent = {'solve': [],
             'date': [],
            'time': [],
            'scramble': [],
            'comments': [],
            'mo3': [],
            'ao5': [],
            'ao12': [],
            'mean': []
            }

def addtime(data,event,date,time,scramble,comments):
    ndata = data.copy()
    ndata[event]['solve'].append(len(ndata[event]['time']))
    ndata[event]['date'].append(date)
    ndata[event]['time'].append(time)
    ndata[event]['scramble'].append(scramble)
    ndata[event]['comments'].append(comments)
    ndata[event]['mo3'].append(calcavg.mean(ndata[event]['time'][-3:]))
    ndata[event]['ao5'].append(calcavg.aox(5,ndata[event]['time']))
    ndata[event]['ao12'].append(calcavg.aox(12,ndata[event]['time']))
    ndata[event]['mean'].append(calcavg.mean(ndata[event]['time']))
    return ndata

def save_data(data):
    with open('times.json','w') as f:
        json.dump(data, f)
        
def get_data():
    file_path = Path('times.json')
    if file_path.exists():
        if file_path.stat().st_size == 0:
            return timedata

        with open(file_path, 'r') as f:
            try:
                content = json.load(f)
                if not content:
                    return timedata
                return content
            except json.JSONDecodeError:
                return timedata
    else:
        return timedata