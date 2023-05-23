import itertools
import re

patterns = [r'(.*)season\d+', r'(.*)s\d+']

strings = ['tutorialsseason1.mkv', 'tutorialsseason2.mkv', 'tutorialsseason13.mkv', 'tutorialsseason12.mkv',
           'pythonseason1.mkv', 'pythons02.mkv', 'javascriptseason1.mkv']


def search(s):
    for p in patterns:
        x = re.findall(p, s.lower())
        if len(x)>0:
            return x[0]
    return ''


iterator = itertools.groupby(strings, lambda x: search(x))
for key, group_list in iterator:
    print(f"{key} -> {list(group_list)}")
