"""import sys
print(sys.argv)
print()
print(sys.path)
print()
print(sys.version)
sys.exit()
print("end")
"""

"""
import platform
print(platform.system())
print()
print(platform.release())
print()
print(platform.processor())
"""
"""
import math
print(math.pi) 
print(math.sin(1/2))
print(math.pow(2,3))
"""
"""
import random

print(random.random())
print(random.randint(1,3))
print(random.uniform(1,3))
"""
"""
import collections
s="python programming"
res=collections.Counter(s)
print(res)
"""
"""
import collections
s='python programming'
d=collections.defaultdict(int)
for i in s:
    d[i]+=1
print(d)
"""
"""
import collections
d=collections.deque([])
d.append(10)
d.append(20)
d.popleft()
d.append(30)
d.popleft()
d.popleft()
d.append(40)
d.append(50)

print(d)
"""
"""
from itertools import combinations,permutations
print(list(combinations("ABCD",3)))
print(list(permutations("ABCD",3)))
"""
