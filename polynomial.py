from itertools import permutations,product 
# Get all permutations
import numpy as np
myS=np.full((3,3,3), 0).tolist()
index=[]
def permutation(arr):
    index=[]
    perm=permutations(arr)
    [index.append(list(i)) for i in list(perm) if list(i) not in index]
    return index


def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

def combine(n,r):
    iterable=[i for i in range(n+1)]
    com=combinations_with_replacement(iterable,r)
    print(com)
    index1=[]
    for i in list(com):
        if n==sum(list(i)):
            [index1.append(el) for el in permutation(list(i))]
    return {"powers":index1,"dimension":len(index1)}


def polynomial(degree,variables):
    powersArray=combine(degree,variables)['powers']
    m=[]
    for powerItems in powersArray:
        term=[(variablesWithPower(i, powerItems[i])) for i in range(variables)]
        m.append(''.join(map(str,term)))
    return '+'.join(map(str,m))
        

# function to convert to subscript
def sub(x):
  base=['\u2080','\u2081','\u2082','\u2083',
         '\u2084','\u2085','\u2086','\u2087',
         '\u2088','\u2089']
  return(base[x])
         
def sup(x):
  power= ['\u2070','\u2071','\u00b2','\u00b3',
         '\u2074','\u2075','\u2076','\u2077',
         '\u2078','\u2079']
  return(power[x])
         
def variablesWithPower(xi,power):
    if power==0:
        return ''
    elif power==1:
        return 'x'+sub(xi)
    else:
        return 'x'+sub(xi)+sup(power)
 

print(polynomial(2, 3))
