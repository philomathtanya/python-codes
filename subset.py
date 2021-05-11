set={1,2,3}
n=2
import itertools
def s(set,n):
    return list (itertools.combinations(set,n))
print(s(set,n))