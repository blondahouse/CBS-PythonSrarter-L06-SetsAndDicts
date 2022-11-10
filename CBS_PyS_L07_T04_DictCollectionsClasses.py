import collections
from collections import OrderedDict
from collections import defaultdict
from collections import ChainMap
import builtins

My_Dict = {'a': 'asdf', 'b': 'bnm,', 'g': 'ghjk', 'z': 'zxcv', 'c': 'cvbn', 'q': 'qwer'}

d = OrderedDict.fromkeys('edcba')
# My_Dict.move_to_end('b')
d.move_to_end('b')
print(d)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(d)

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
print(d)

pylookup = ChainMap(locals(), globals(), vars(builtins))
print(pylookup)
