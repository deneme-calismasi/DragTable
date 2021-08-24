import numpy as np
import pandas as pd

aggregation_list = [
    {'a': 1, 'b': 2, 'c': 3},
    {'a': 4, 'b': 5, 'c': 6},
    {'a': 7, 'b': 8, 'c': 9}
]

df = pd.DataFrame.from_records(aggregation_list)

a = np.array(df['a'])
b = np.array(df['b'])
c = np.array(df['c'])

print(a)
print(b)
print(c)

dicts = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}, {'x': 7, 'y': 8, 'z': 9}]

x, y, z = np.array(list(zip(*map(dict.values, dicts))))

print(x)

t = np.array(list(zip(*map(dict.values, dicts))))

print(t)
