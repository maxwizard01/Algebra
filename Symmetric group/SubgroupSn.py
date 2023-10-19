def Combine(arr,no):
    from itertools import combinations
    # Input list of elements
    #elements = ["F","F","F","F","F","B","B","B","B","B"]
    elements =arr
    # Specify the size of combinations you want to generate
    combination_size = no

    # Generate all combinations of the elements
    combinations_list = list(combinations(elements, combination_size))
    return set(combinations_list)

   
def permuteA(em):   
    from itertools import permutations
    return [list(i) for i in list(permutations(em))]
        
def Sn(n):
    array=[i for i in range(n)]
    return permuteA(array)

def Cyc(arr):
    newCyc=[]
    domain=0
    for element in arr:
        image=arr[domain]
        if(image==domain or (image in newCyc)):
            break
        else:
            newCyc.append(image)
            domain=image
    if(len(newCyc)==len(arr)):
       return newCyc

def convertToCyc(arr,start):
    newCyc=[[] for i in arr]
    newCyc[0].append(0)
    currentCyc=0
    domain=0
    remainingArr=[i for i in range(1,len(arr))]
    for element in arr:
        image=arr[domain]
        if(len(remainingArr)==0):
            break
        elif(image in newCyc[currentCyc]):
            currentCyc+=1
            image=remainingArr[0]
            newCyc[currentCyc].append(image)
            domain=image
            remainingArr.remove(image)
           
        else:
            newCyc[currentCyc].append(image)
            remainingArr.remove(image)
            domain=image
        
        
    return [i for i in newCyc if len(i)>start ]

def ConvertSnToCyc(sn,inc1udeOne):
    newForm=[convertToCyc(element,inc1udeOne) for element in sn]
    return newForm
    
def CycSn(n):
    newOne=[]
    for element in Sn(n):
        newOne.append(Cyc(element))
    return newOne

def lengthCategorize(arr):
    newArr=[]
    for element in arr:
        sortlength=[len(i) for i in element]
        #sortlength.sort()
        newArr.append(sortlength)
    return newArr

def CycCategorize(arr):
    lengthCategorized=lengthCategorize(arr)
    cyclic=[]
    NonCyclic=[]
    for i in range(len(arr)):
        if(len(lengthCategorized[i])==1):
            cyclic.append(arr[i])
        else:
            NonCyclic.append(arr[i])
    return {"cyclic":cyclic,"noncyclic":NonCyclic}

def removeDuplicate(arr):
    newOne=[]
    for i in arr:
        if(i not in newOne):
            newOne.append(i)
    return newOne

def noOfDisjointInNonCyc(nonCyc):
    return [len(disjoint) for disjoint in nonCyc]

def hcf(a,b):
    hcf=1
    for i in range(1,max(int(a),int(b))+1):
        if a%i == b%i==0:
            hcf=i
    return hcf

def lcm(a,b):
    return a*b/hcf(a,b)

def lcmMany(arr):
    if len(arr)==0:
        return 0
    else:
        first=arr[0]
        if len(arr)<2:
            return first
        else:
            for i in range(1,len(arr)):
                first=lcm(first,arr[i])
                return first


def possiblePerm(cycArr):
    m=lengthCategorize(cycArr)
    keys=removeDuplicate(m)
    j={}
    for key in keys:
        j[str(key)]=0
    for element in m:
        j[str(element)]+=1
    return j

def OrderCategoryInSn(cycArr):
    m=lengthCategorize(cycArr)
    return [lcmMany(i) for i in m]

def ArrToObj(Arr):
    keys=removeDuplicate(Arr)
    j={}
    for key in keys:
        j[str(key)]=0
    for element in Arr:
        j[str(element)]+=1
    return j

##for i in range(3,10):
##    newSn=Sn(i)
##    j=ConvertSnToCyc(newSn,1)
##    #m= CycCategorize(j)['noncyclic']
##    #print(possiblePerm(m))#)
##    n= CycCategorize(j)['cyclic']
##    disjoint=noOfDisjointInNonCyc(n)
##    obj=ArrToObj(OrderCategoryInSn(n))

#print(m)
#print(m)
def sequ(arr):
    lengthCategorized=lengthCategorize(arr)
    unique=removeDuplicate(lengthCategorized)
    freq=[lengthCategorized.count(i) for i in unique  ]
    return [unique,freq]


def FacePermute(arr,n):
    transform=[removeDuplicate(permuteA(i))for i in set(Combine(arr,n))]
    return [j for i in transform for j in i]

def MargeTwoArr(arr1,arr2):
    return [arr1[i]+"_"+str(arr2[i]) for i in range(len(arr1))]

def MergeGroupFaces(FacePermutation,position):
    return [MargeTwoArr(faces,position) for faces in FacePermutation]

factorial=lambda n: 1 if n<2 else n*factorial(n-1)#factoria function
FaceCa=lambda n,f:factorial(n)*f**n
n=["A","A","A","A","A","B","B","B","B","B","B","B","C","C","C","C","C","C","D","D","D","D","D","D"]

i=[1,2]
r=MergeGroupFaces(FacePermute(n,2),i)
#print(FaceCa(5,3))
r=FacePermute(n,4)
#print(r)
j=[['black!6',1, 'black!30',2], ['black!30',1, 'black!6',2], ['black!30',1, 'black!30',2], ['black!6',1, 'black',2], ['black',1, 'black!6',2], ['white',1, 'white',2], ['black!30',1, 'black',2], ['black',1, 'black!30',2], ['white',1, 'black!30',2], ['black!30',1, 'white',2], ['black!6',1, 'black!6',2], ['white',1, 'black',2], ['black',1, 'white',2], ['black',1, 'black',2], ['white',1, 'black!6',2], ['black!6',1, 'white',2]]

def coor(arr):
    return "\item  \ twoFaceTwo{"+ arr[0]+ "}{Front}{" + str(arr[1])+"}{" + arr[2]+ "}{Front}{"+ str(arr[3]) +"}"
#for i in j:
   # print(coor(i))


def operate(a,b):
    return [a[i] for i in b]

def CheckClosure(arr):
    result=True
    wrongPerm=[]
    for element1 in arr:
        for element2 in arr:
            newElement=operate(element1,element2)
            if newElement not in arr:
                result=False
                wrongPerm=[element1,element2]
        if result ==False:
            break
    return {"resul":result,"Perm":wrongPerm}


def groupOfSameCyc(Arr,cycType):
    group=[]
    index=0
    allTypeOfCyc=lengthCategorize(ConvertSnToCyc(Arr,1))
    for PerticularType in allTypeOfCyc:
        if(PerticularType==cycType):
            group.append(Arr[index])
        index=index+1
    return group

def CategoryOfCyce(arr,allTypeOfCycArr):
    for TypeOfCyc in allTypeOfCycArr:
        print(str(TypeOfCyc ))
        print(groupOfSameCyc(arr,TypeOfCyc))

p=Sn(4+1)
q=ConvertSnToCyc(p,1)
m=lengthCategorize(q)
t=[[2],[3],[3,2],[2,2],[5],[4]]

#CategoryOfCyce(p,t)
u=[[[0,1,2,3,4],[0, 1, 2, 4, 3], [0, 1, 3, 2, 4], [0, 1, 4, 3, 2], [0, 2, 1, 3, 4], [0, 3, 2, 1, 4], [0, 4, 2, 3, 1], [1, 0, 2, 3, 4], [2, 1, 0, 3, 4], [3, 1, 2, 0, 4], [4, 1, 2, 3, 0]],

[[0,1,2,3,4],[0, 1, 3, 4, 2], [0, 1, 4, 2, 3], [0, 2, 3, 1, 4], [0, 2, 4, 3, 1], [0, 3, 1, 2, 4], [0, 3, 2, 4, 1], [0, 4, 1, 3, 2], [0, 4, 2, 1, 3], [1, 2, 0, 3, 4], [1, 3, 2, 0, 4], [1, 4, 2, 3, 0], [2, 0, 1, 3, 4], [2, 1, 3, 0, 4], [2, 1, 4, 3, 0], [3, 0, 2, 1, 4], [3, 1, 0, 2, 4], [3, 1, 2, 4, 0], [4, 0, 2, 3, 1], [4, 1, 0, 3, 2], [4, 1, 2, 0, 3]],

[[1, 2, 0, 4, 3], [1, 3, 4, 0, 2], [1, 4, 3, 2, 0], [2, 0, 1, 4, 3], [2, 3, 4, 1, 0], [2, 4, 3, 0, 1], [3, 0, 4, 1, 2], [3, 2, 1, 4, 0], [3, 4, 0, 2, 1], [4, 0, 3, 2, 1], [4, 2, 1, 0, 3], [4, 3, 0, 1, 2],[1, 0, 3, 4, 2], [1, 0, 4, 2, 3], [2, 3, 0, 4, 1], [2, 4, 0, 1, 3], [3, 2, 4, 0, 1], [3, 4, 1, 0, 2], [4, 2, 3, 1, 0], [4, 3, 1, 2, 0],[0,1,2,3,4]],

[[0,1,2,3,4],[0, 2, 1, 4, 3], [0, 3, 4, 1, 2], [0, 4, 3, 2, 1], [1, 0, 2, 4, 3], [1, 0, 3, 2, 4], [1, 0, 4, 3, 2], [2, 1, 0, 4, 3], [2, 3, 0, 1, 4], [2, 4, 0, 3, 1], [3, 1, 4, 0, 2], [3, 2, 1, 0, 4], [3, 4, 2, 0, 1], [4, 1, 3, 2, 0], [4, 2, 1, 3, 0], [4, 3, 2, 1, 0]],

[[0,1,2,3,4],[1, 2, 3, 4, 0], [1, 2, 4, 0, 3], [1, 3, 0, 4, 2], [1, 3, 4, 2, 0], [1, 4, 0, 2, 3], [1, 4, 3, 0, 2], [2, 0, 3, 4, 1], [2, 0, 4, 1, 3], [2, 3, 1, 4, 0], [2, 3, 4, 0, 1], [2, 4, 1, 0, 3], [2, 4, 3, 1, 0], [3, 0, 1, 4, 2], [3, 0, 4, 2, 1], [3, 2, 0, 4, 1], [3, 2, 4, 1, 0], [3, 4, 0, 1, 2], [3, 4, 1, 2, 0], [4, 0, 1, 2, 3], [4, 0, 3, 1, 2], [4, 2, 0, 1, 3], [4, 2, 3, 0, 1], [4, 3, 0, 2, 1], [4, 3, 1, 0, 2]],

[[0,1,2,3,4],[0, 2, 3, 4, 1], [0, 2, 4, 1, 3], [0, 3, 1, 4, 2], [0, 3, 4, 2, 1], [0, 4, 1, 2, 3], [0, 4, 3, 1, 2], [1, 2, 3, 0, 4], [1, 2, 4, 3, 0], [1, 3, 0, 2, 4], [1, 3, 2, 4, 0], [1, 4, 0, 3, 2], [1, 4, 2, 0, 3], [2, 0, 3, 1, 4], [2, 0, 4, 3, 1], [2, 1, 3, 4, 0], [2, 1, 4, 0, 3], [2, 3, 1, 0, 4], [2, 4, 1, 3, 0], [3, 0, 1, 2, 4], [3, 0, 2, 4, 1], [3, 1, 0, 4, 2], [3, 1, 4, 2, 0], [3, 2, 0, 1, 4], [3, 4, 2, 1, 0], [4, 0, 1, 3, 2], [4, 0, 2, 1, 3], [4, 1, 0, 2, 3], [4, 1, 3, 0, 2], [4, 2, 0, 3, 1], [4, 3, 2, 0, 1]]]

#for i in u:
    #print(CheckClosure(i))
    #print(len(i))

##{'resul': False, 'Perm': [[0, 1, 2, 4, 3], [4, 1, 2, 3, 0]]}
##11
##{'resul': False, 'Perm': [[0, 1, 3, 4, 2], [4, 1, 0, 3, 2]]}
##21
##{'resul': False, 'Perm': [[1, 2, 0, 4, 3], [4, 3, 1, 2, 0]]}
##21
##{'resul': False, 'Perm': [[0, 2, 1, 4, 3], [4, 3, 2, 1, 0]]}
##16
##{'resul': False, 'Perm': [[1, 2, 3, 4, 0], [4, 3, 1, 0, 2]]}
##25
##{'resul': False, 'Perm': [[0, 2, 3, 4, 1], [4, 3, 2, 0, 1]]}
##31

r=[[0, 2, 1, 4, 3], [0, 3, 4, 1, 2], [0, 4, 3, 2, 1], [1, 0, 2, 4, 3], [1, 0, 3, 2, 4], [1, 0, 4, 3, 2], [2, 1, 0, 4, 3], [2, 3, 0, 1, 4], [2, 4, 0, 3, 1], [3, 1, 4, 0, 2], [3, 2, 1, 0, 4], [3, 4, 2, 0, 1], [4, 1, 3, 2, 0], [4, 2, 1, 3, 0], [4, 3, 2, 1, 0],[0,1,2,3,4],[1, 2, 3, 4, 0], [1, 2, 4, 0, 3], [1, 3, 0, 4, 2], [1, 3, 4, 2, 0], [1, 4, 0, 2, 3], [1, 4, 3, 0, 2], [2, 0, 3, 4, 1], [2, 0, 4, 1, 3], [2, 3, 1, 4, 0], [2, 3, 4, 0, 1], [2, 4, 1, 0, 3], [2, 4, 3, 1, 0], [3, 0, 1, 4, 2], [3, 0, 4, 2, 1], [3, 2, 0, 4, 1], [3, 2, 4, 1, 0], [3, 4, 0, 1, 2], [3, 4, 1, 2, 0], [4, 0, 1, 2, 3], [4, 0, 3, 1, 2], [4, 2, 0, 1, 3], [4, 2, 3, 0, 1], [4, 3, 0, 2, 1], [4, 3, 1, 0, 2],
   [1, 2, 0, 4, 3], [1, 3, 4, 0, 2], [1, 4, 3, 2, 0], [2, 0, 1, 4, 3], [2, 3, 4, 1, 0], [2, 4, 3, 0, 1], [3, 0, 4, 1, 2], [3, 2, 1, 4, 0], [3, 4, 0, 2, 1], [4, 0, 3, 2, 1], [4, 2, 1, 0, 3], [4, 3, 0, 1, 2],[1, 0, 3, 4, 2], [1, 0, 4, 2, 3], [2, 3, 0, 4, 1], [2, 4, 0, 1, 3], [3, 2, 4, 0, 1], [3, 4, 1, 0, 2], [4, 2, 3, 1, 0], [4, 3, 1, 2, 0]]


print(CheckClosure(r))
##r=[[0, 2, 1, 4, 3], [0, 3, 4, 1, 2], [0, 4, 3, 2, 1], [1, 0, 2, 4, 3], [1, 0, 3, 2, 4], [1, 0, 4, 3, 2], [2, 1, 0, 4, 3],
    ##[2, 3, 0, 1, 4], [2, 4, 0, 3, 1], [3, 1, 4, 0, 2], [3, 2, 1, 0, 4], [3, 4, 2, 0, 1], [4, 1, 3, 2, 0], [4, 2, 1, 3, 0],
    ##[4, 3, 2, 1, 0],[0,1,2,3,4],[1, 2, 3, 4, 0], [1, 2, 4, 0, 3], [1, 3, 0, 4, 2], [1, 3, 4, 2, 0], [1, 4, 0, 2, 3],
    ##[1, 4, 3, 0, 2], [2, 0, 3, 4, 1], [2, 0, 4, 1, 3], [2, 3, 1, 4, 0], [2, 3, 4, 0, 1], [2, 4, 1, 0, 3], [2, 4, 3, 1, 0], [3, 0, 1, 4, 2],
    ##[3, 0, 4, 2, 1], [3, 2, 0, 4, 1], [3, 2, 4, 1, 0], [3, 4, 0, 1, 2], [3, 4, 1, 2, 0], [4, 0, 1, 2, 3], [4, 0, 3, 1, 2],
    ##[4, 2, 0, 1, 3], [4, 2, 3, 0, 1], [4, 3, 0, 2, 1], [4, 3, 1, 0, 2]]
##{'resul': False, 'Perm': [[0, 2, 1, 4, 3], [4, 2, 0, 1, 3]]}
##len(r)
##40


##{'resul': False, 'Perm': [[0, 2, 1, 4, 3], [4, 3, 1, 2, 0]]}

##r=[[0, 2, 1, 4, 3], [0, 3, 4, 1, 2], [0, 4, 3, 2, 1], [1, 0, 2, 4, 3], [1, 0, 3, 2, 4], [1, 0, 4, 3, 2], [2, 1, 0, 4, 3], [2, 3, 0, 1, 4], [2, 4, 0, 3, 1], [3, 1, 4, 0, 2], [3, 2, 1, 0, 4], [3, 4, 2, 0, 1], [4, 1, 3, 2, 0], [4, 2, 1, 3, 0], [4, 3, 2, 1, 0],[0,1,2,3,4],[1, 2, 3, 4, 0], [1, 2, 4, 0, 3], [1, 3, 0, 4, 2], [1, 3, 4, 2, 0], [1, 4, 0, 2, 3], [1, 4, 3, 0, 2], [2, 0, 3, 4, 1], [2, 0, 4, 1, 3], [2, 3, 1, 4, 0], [2, 3, 4, 0, 1], [2, 4, 1, 0, 3], [2, 4, 3, 1, 0], [3, 0, 1, 4, 2], [3, 0, 4, 2, 1], [3, 2, 0, 4, 1], [3, 2, 4, 1, 0], [3, 4, 0, 1, 2], [3, 4, 1, 2, 0], [4, 0, 1, 2, 3], [4, 0, 3, 1, 2], [4, 2, 0, 1, 3], [4, 2, 3, 0, 1], [4, 3, 0, 2, 1], [4, 3, 1, 0, 2],
##  [0,1,2,3,4],[0, 1, 3, 4, 2], [0, 1, 4, 2, 3], [0, 2, 3, 1, 4], [0, 2, 4, 3, 1], [0, 3, 1, 2, 4], [0, 3, 2, 4, 1], [0, 4, 1, 3, 2], [0, 4, 2, 1, 3], [1, 2, 0, 3, 4], [1, 3, 2, 0, 4], [1, 4, 2, 3, 0], [2, 0, 1, 3, 4], [2, 1, 3, 0, 4], [2, 1, 4, 3, 0], [3, 0, 2, 1, 4], [3, 1, 0, 2, 4], [3, 1, 2, 4, 0], [4, 0, 2, 3, 1], [4, 1, 0, 3, 2], [4, 1, 2, 0, 3]]
## {'resul': True, 'Perm': []}
##len(r)
##60


##r=[[0, 2, 1, 4, 3], [0, 3, 4, 1, 2], [0, 4, 3, 2, 1], [1, 0, 2, 4, 3], [1, 0, 3, 2, 4], [1, 0, 4, 3, 2], [2, 1, 0, 4, 3], [2, 3, 0, 1, 4], [2, 4, 0, 3, 1], [3, 1, 4, 0, 2], [3, 2, 1, 0, 4], [3, 4, 2, 0, 1], [4, 1, 3, 2, 0], [4, 2, 1, 3, 0], [4, 3, 2, 1, 0],[0,1,2,3,4],[1, 2, 3, 4, 0], [1, 2, 4, 0, 3], [1, 3, 0, 4, 2], [1, 3, 4, 2, 0], [1, 4, 0, 2, 3], [1, 4, 3, 0, 2], [2, 0, 3, 4, 1], [2, 0, 4, 1, 3], [2, 3, 1, 4, 0], [2, 3, 4, 0, 1], [2, 4, 1, 0, 3], [2, 4, 3, 1, 0], [3, 0, 1, 4, 2], [3, 0, 4, 2, 1], [3, 2, 0, 4, 1], [3, 2, 4, 1, 0], [3, 4, 0, 1, 2], [3, 4, 1, 2, 0], [4, 0, 1, 2, 3], [4, 0, 3, 1, 2], [4, 2, 0, 1, 3], [4, 2, 3, 0, 1], [4, 3, 0, 2, 1], [4, 3, 1, 0, 2],
   ##[1, 2, 0, 4, 3], [1, 3, 4, 0, 2], [1, 4, 3, 2, 0], [2, 0, 1, 4, 3], [2, 3, 4, 1, 0], [2, 4, 3, 0, 1], [3, 0, 4, 1, 2], [3, 2, 1, 4, 0], [3, 4, 0, 2, 1], [4, 0, 3, 2, 1], [4, 2, 1, 0, 3], [4, 3, 0, 1, 2],[1, 0, 3, 4, 2], [1, 0, 4, 2, 3], [2, 3, 0, 4, 1], [2, 4, 0, 1, 3], [3, 2, 4, 0, 1], [3, 4, 1, 0, 2], [4, 2, 3, 1, 0], [4, 3, 1, 2, 0]]
## {'resul': False, 'Perm': [[0, 2, 1, 4, 3], [4, 3, 1, 2, 0]]}
##len(r)
##60

