from itertools import permutations,product 
# Get all permutations
import numpy as np

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

# function to convert to subscript
def sub(x):
    base=['\u2080','\u2081','\u2082','\u2083','\u2084','\u2085','\u2086','\u2087','\u2088','\u2089']
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
 
class Polynomials:
  def __init__(self, deg, var):
    self.degree = deg
    self.variable = var
    self.Basis=self.Basis()
    self.Dimension=len(self.Basis)
    self.function='+'.join(map(str,self.Basis))
  
  def Basis(self):
      degree=self.degree
      variables=self.variable
      powersArray=self.combine()
      m=[]
      for powerItems in powersArray:
          term=[(variablesWithPower(i, powerItems[i])) for i in range(variables)]
          m.append(''.join(map(str,term)))
      return m
  
  def combine(self):
      n=self.degree
      r=self.variable
      
      iterable=[i for i in range(n+1)]
      com=combinations_with_replacement(iterable,r)
      index1=[]
      for i in list(com):
          if n==sum(list(i)):
              [index1.append(el) for el in permutation(list(i))]
      return index1


 
x = Polynomials(2,3)
print(x.Dimension)
