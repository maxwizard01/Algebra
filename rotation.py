
class Symmetric:
    def __init__(self, deg, var):
        self.order = deg
        self.vector = var
        self.Tensor=self.Tensor()['0']
        self.Basis=self.Tensor()['1']
        self.Dimension=len(self.uniqueIndex())
        
        
    
    def permute(self,arr):
        index=[]
        perm=permutations(arr)
        [index.append(tuple(i)) for i in tuple(perm) if tuple(i) not in index]
        return index
    
    def uniqueIndex(self):
        k=[i for i in range(self.vector)]
        r=[i for i in combinations_with_replacement(k,self.order)]
        return r  
    
    def Tensor(self):
        vector=self.vector
        order=self.order
        import numpy as np
        shape = (vector,)*order  # 2 layers, 3 rows, 4 columns
        # Define the string to fill the array
        fill_value = 'text'
        # Create the n-dimensional array with the same string as entry
        arr = np.full(shape,'text' )
        k=[i for i in range(vector)]
        r=combinations_with_replacement(k,order)
        d=np.array([self.permute(j) for j in r],dtype=object)
        basis=[]
        nutIndex=0
        for t in d:
            basisElementPattern=np.full(shape,0 )
            print(basisElementPattern)
            for m in t:
                item='a'+sub(nutIndex)
                arr[m]=''.join(item)
                basisElementPattern[m]=1
            nutIndex+=1
            basis.append(basisElementPattern)

        return {'0':arr,'1':basis}
    
from itertools import permutations,product 
# Get all permutations
import numpy as np

def permutation(arr):
    index=[]
    perm=permutations(arr)
    [index.append(list(i)) for i in list(perm) if list(i) not in index]
    return index


# function to convert to subscript
def sub(x):
    base=['\u2080','\u2081','\u2082','\u2083','\u2084','\u2085','\u2086','\u2087','\u2088','\u2089']
    subscritptFigure=''.join(map(str,[base[int(i)] for i in list(str(x))]))
    return subscritptFigure
         
def sup(x):
  power= ['\u2070','\u2071','\u00b2','\u00b3',
         '\u2074','\u2075','\u2076','\u2077',
         '\u2078','\u2079']
  superscritp=''.join(map(str,[power[int(i)] for i in list(str(x))]))
    
  return superscritp
     

def subs(x):
    return '_{'+str(x)+'}'
def sups(x):
    return '^{'+str(x)+'}'

    
def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)


def variablesWithPower(xi,power):
    if power==0:
        return ''
    elif power==1:
        return 'x'+sub(xi)
    else:
        return 'x'+sub(xi)+sup(power)
 
def addCoefficient(arr):
    arrWithCoefficient=[]
    nuts=[i for i in range(len(arr))]
    for i in nuts:
        coefficienWithVariable='a'+sub(i)+str(arr[i])
        arrWithCoefficient.append(coefficienWithVariable)
    return arrWithCoefficient

class Homogeneous:
  def __init__(self, deg, var):
    self.degree = deg
    self.variable = var
    self.Basis=self.Basis()
    self.Dimension=len(self.Basis)
    self.Function='+'.join(map(str,addCoefficient( self.Basis)))+'=0'
  
  def __repr__(self):
      return self.function
    
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
  
 

class SymmetricTensors:
    def __init__(self, deg, var):
        self.order = deg
        self.vector = var
        self.Tensor=self.Tensor()
        self.Dimension=len(self.uniqueIndex())
        
    
    def permute(self,arr):
        index=[]
        perm=permutations(arr)
        [index.append(tuple(i)) for i in tuple(perm) if tuple(i) not in index]
        return index
    
    def uniqueIndex(self):
        k=[i for i in range(self.vector)]
        r=[i for i in combinations_with_replacement(k,self.order)]
        return r
    
    
    def Tensor(self):
        vector=self.vector
        order=self.order
        import numpy as np
        shape = (vector,)*order  # 2 layers, 3 rows, 4 columns
        # Define the string to fill the array
        fill_value = 'text'
        # Create the n-dimensional array with the same string as entry
        arr = np.full(shape,'text' )
        k=[i for i in range(vector)]
        r=combinations_with_replacement(k,order)
        d=np.array([self.permute(j) for j in r],dtype=object)
        difference=0
        for t in d:
            for m in t:
                item='a'+sub(difference)
                arr[m]=''.join(item)
            difference+=1

        return arr
        #for index, value in np.ndenumerate(m):
        #m[index] = value + 1


##TESTING THE MODUE
class Polynomials:
  def __init__(self, deg, var):
    import math
    self.degree = deg
    self.variable = var
    self.Basis=self.Basis()
    self.Basis[0]=1
    self.Dimension=len(self.Basis)
    self.Function='+'.join(map(str,addCoefficient(self.Basis))).replace('a₀1','a₀')
  
  def Basis(self):
      degree=self.degree
      variables=self.variable
      powersArray=self.combine()
      m=[]
      for powerItems in powersArray:
          term=[(variablesWithPower(i, powerItems[i])) for i in range(variables)]
          m.append(''.join(map(str,term)))
      m[0]=1
      return m
      
  def combine(self):
      n=self.degree
      r=self.variable 
      iterable=[i for i in range(n+1)]
      com=combinations_with_replacement(iterable,r)
      index1=[]
      for i in list(com):
          if (sum(list(i))<=n):
              [index1.append(el) for el in permutation(list(i))]
      return index1
  
#Testing the Codes for Symmetric Tensor
#for i in range(2,8):
 #   M=SymmetricTensors(3, i)
  #  print(M.Dimension)

#Testing the Codes for Homogenous
#for i in range(2,8):
 #   M=Homogeneous(3, i)
  #  print(M.Basis)
  #  print(M.Dimension)

#Testing the Codes for polynomials
# for i in range(2,7):
#     M=Polynomials(3, i)
#     print(M.Basis)








def rotation(arr,theta):
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Define the rotation angle
    theta = np.pi *theta
    
    # Define the vector to be rotated
    v = np.array(arr)
    
    # Calculate the rotation matrix
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    
    # Calculate the rotated vector
    w = np.dot(R, v)
    
    # Plot the vectors before and after rotation
    plt.arrow(0, 0, v[0], v[1], head_width=0.1, head_length=0.1, color='r',label='origina')
    plt.arrow(0, 0, w[0], w[1], head_width=0.1, head_length=0.1, color='b',label='Refection')
    plt.xlim(-5, 15)
    plt.ylim(-5, 15)
    plt.text(v[0], v[1], 'Original', ha='center', va='bottom', fontsize=12, color='r')
    plt.text(w[0], w[1], 'Reflection', ha='center', va='bottom', fontsize=10, color='b')

# Add a legend to the chart
    plt.legend()
    plt.grid()
    plt.show()


def reflection(arr,axis):
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Define the reflection axis
    v = np.array(axis)
    v = v / np.linalg.norm(v)
    
    # Define the vector to be reflected
    w = np.array(arr)
    
    # Calculate the projection of w onto v
    proj = np.dot(w, v) * v
    
    # Calculate the reflection of w
    refl = 2 * proj - w
    
    # Plot the vectors and the reflection axis
    plt.arrow(0, 0, v[0], v[1], head_width=0.1, head_length=0.1, color='b')
    plt.arrow(0, 0, w[0], w[1], head_width=0.1, head_length=0.1, color='r')
    plt.arrow(0, 0, refl[0], refl[1], head_width=0.1, head_length=0.1, color='g')
    plt.xlim(-15, 15)
    plt.ylim(-15, 15)
    plt.text(v[0], v[1], 'Original', ha='center', va='bottom', fontsize=12, color='r')
    plt.text(w[0], w[1], 'Reflection', ha='center', va='bottom', fontsize=10, color='b')

    plt.grid()
    plt.show()
    
#Testing Refection on Y-axis
for i in  range(13):
    reflection([2,i],[0,1])

#Testing Refection on X-axis
for i in  range(13):
    reflection([2,i],[1,0])

#Testing Refection on Y-axis
for i in  range(13):
    rotation([2,i],[0,1])

#Testing Refection on X-axis
for i in  range(13):
    rotation([2,i],[1,0])
