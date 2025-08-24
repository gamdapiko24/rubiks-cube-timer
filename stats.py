# stats.py

from math import e
import calcavg

class Commands:
    def __init__(self, times):
        self.times = times
    
        self.commands = {
            'stats_from_index': self.stats_from_index,
            'best': self.best,
            'worst': self.worst,
            'list_times': self.list_times,
            'search_times': self.search_times,
            'sort_best': self.sort_best,
            }
    
    def pretty_dictionary(self, d):
        final = ''
        for key, value in d.items():
            final += f'{key}: {value}\n'
        return final

    def get_stats_from(self, index):
        stats = {}
        keys_list = list(self.times.keys())
        for stat_key in keys_list:
            stats[stat_key] = self.times[stat_key][index]
        return stats
            
    
    def execute(self, command):
        func = self.commands.get(command)
        if func:
            return func()
        else:
            return f'Unknown command: {command}'
    
    def stats_from_index(self, index=None):
        if index is None:
            while True:
                try:
                    index = int(input('What index?').strip())
                    break
                except ValueError:
                    print('Please enter an number')

        return self.pretty_dictionary(self.get_stats_from(index))

    def best(self):
        while True:
            try:
                t = input('Best what? (time, mo3, ao5, ao12, mean)').strip()
                def value_or_inf(val):
                    if isinstance(val, str) and val.strip().upper() in ('DNF','N/A'):
                        return float('inf')
                    return float(val)

                values = self.times[t]
                best_index = min(range(len(values)), key=lambda i: value_or_inf(values[i]))
                return self.stats_from_index(best_index)
            except KeyError:
                print('Please choose one of the options')

    
    def worst(self):
        while True:
            try:
                t = input('Worst what? (time, mo3, ao5, ao12, mean)').strip()
                def value_or_inf(val):
                    if isinstance(val, str) and val.strip().upper() in ('DNF','N/A'):
                        return float('inf')
                    return float(val)

                values = self.times[t]
                worst_index = max(range(len(values)), key=lambda i: value_or_inf(values[i]))
                return self.stats_from_index(worst_index)
            except KeyError:
                print('Please choose one of the options')

    def list_times(self):
        pretty_list = ''
        for i in range(len(self.times['time'])):
            pretty_list += self.stats_from_index(i)
            pretty_list += '\n'
        return pretty_list

    def search_times(self):
        while True:
            try:
                search = float(input('What time would you like to search?').strip())
                break
            except ValueError:
                print('Please input a float')

        indexes = []
        for i, x in enumerate(self.times['time']):
            if isinstance(x, str) and x.strip().upper() in ('DNF','N/A'):
                continue
            try:
                if abs(float(x) - search) < 1e-6:
                    indexes.append(i)
            except ValueError:
                continue

        if not indexes:
            print(f'{search} not found')
        
        pretty_list = ''
        for i in indexes:
            pretty_list += self.stats_from_index(i)
            pretty_list += '\n'
        return pretty_list

    def sort_best(self):
        while True:
            try:
                t = input('Sort by what? (time, mo3, ao5, ao12, mean)').strip()
                def get_sort_value(i):
                    value = self.times[t][i]
                    if isinstance(value, str) and value.strip().upper() in ('DNF', 'N/A'):
                        return float('inf')
                    return float(value)
                sorted_idxs = sorted(range(len(self.times[t])), key=get_sort_value)
                break
            except KeyError:
                print('Please choose one of the options')
        pretty_list = ''
        for i1 in sorted_idxs:
            pretty_list += self.stats_from_index(i1)
            pretty_list += '\n'
        return pretty_list

