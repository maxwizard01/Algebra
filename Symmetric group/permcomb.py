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
    return list(permutations(em)
        
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

def CycSn(n):
    newOne=[]
    for element in Sn(n):
        newOne.append(Cyc(element))
    return newOne
for i in range(2,7):
    print(CycSn(i))
