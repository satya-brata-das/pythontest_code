import itertools
def sum(vals,target):
    return tuple(sorted([(a,b) for a,b in itertools.combinations(vals,2) if a+b == target]))
    
print(sum([3,2,6,1,5,4],7)