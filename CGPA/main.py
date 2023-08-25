
import pandas as pd
import numpy as np
import matplotlib.pyplot as mpt
arabic=pd.read_csv('Arts1.csv')['CGPA']
arabic100=pd.read_excel('Arts.xlsx',None)
arabic200=pd.read_excel('Arts.xlsx',sheet_name='arabic200')['CGPA']
arabic300=pd.read_excel('Arts.xlsx',sheet_name='arabic300')['CGPA']
#print(arabic100.keys())

#print(np.array(arabic200))
#print(np.array(arabic100))
def pieChart(arrayData,title):
    percentageData=np.round(np.array(arrayData[0])*100/ sum(arrayData[0]),1)
    percentage_label=[str(percentageData[i])+"%" for i in range(len(arrayData[0]))]
    mpt.pie(arrayData[0],labels=percentage_label)
    mpt.legend(arrayData[1], loc= "lower left",fontsize=11)
    mpt.title(title)

def Histogram(arrayData,title):
    mpt.hist(arrayData[0])
    mpt.title(title)

def Categorize(arrayData):
    firstClass=[]
    secondClassUpper=[]
    secondClassLower=[]
    thirdClass=[]
    withdraw=[]
    for i in arrayData:
        if float(i)>=3.5:
            firstClass.append(i)
        elif float(i)>=3.0:
            secondClassUpper.append(i)
        elif float(i)>=2.0:
            secondClassLower.append(i)
        elif float(i)>=1.0:
            thirdClass.append(i)
        else:
            withdraw.append(i)
    Grades=[len(firstClass), len(secondClassUpper), len(secondClassLower),len(thirdClass),len(withdraw)]
    labels = ["firstClass", "secondClassUpper", "secondClassLower", "thirdClass", "withdraw"]
    return [Grades,labels]

#Histogram(Categorize(arabic100),"Category of Students in Arabic (100L)")

#mpt.subplot(1, 3, 1)
#pieChart(Categorize(arabic100),"100L")
#mpt.subplot(1, 3, 2)
#pieChart(Categorize(arabic200),"200L")
#mpt.subplot(1, 3, 3)
#pieChart(Categorize(arabic300),"300 Leve")
#mpt.suptitle("CGPA GRAPH OF ARABIC DEPARTMENT")
#mpt.show()


def mySheets(excelName):
    excel = pd.read_excel(excelName, None)
    sheetNames=excel.keys()
    Data={"sheetNames":list(sheetNames)}
    for sheet in sheetNames:
        Data[sheet]= pd.read_excel(excelName,sheet_name=sheet)
    return Data



def ExtractCgpa(excelSheet):
    allDataInExcel=mySheets(excelSheet)
    CGPA={}
    for sheet in allDataInExcel["sheetNames"]:
        CGPA[sheet]=allDataInExcel[sheet]["CGPA"]
    return CGPA
    

    
def CategorizeCgpa(excelSheet):
    categoryOfDepartments={}
    cgpaData=ExtractCgpa(excelSheet)
    departmentNames=cgpaData.keys()
    for department in departmentNames:
        categoryOfDepartments[department]=Categorize(cgpaData[department])
    return categoryOfDepartments
        

 
import matplotlib.pyplot as plt
def MutipleBar(excel='Arts.xlsx',start=0,end=3,title="Arabic and Archaeology CGPA Bar Chart"):
    data=CategorizeCgpa(excel)
    
    cgpaArray=[]
    Departmentlabel=list(data.keys())[start:end]
    X_axis1=np.arange(4+1)
    numbersOfDepartment=end-start
    k=len(Departmentlabel)
    for i in range(len(Departmentlabel)):
        label=Departmentlabel[i]
        width=0.94/numbersOfDepartment
        X_axis=np.arange(4+1)-(len(Departmentlabel)-1)/2*width
        #plt.bar(X_axis-0.08*(i+0.01)*(-1)**i,data[label][0],0.23,label=label)
        plt.bar(X_axis+width*i,np.array(data[label][0])+0.17,width,label=label)
    plt.xticks(X_axis1,["firstClass", "secondClassUpp", ". secondClassLow", "thirdClass", "withdrawn"],fontsize="5")
    #plt.xlabel("Category of Honour")
    plt.ylabel("Number of Students")
    plt.title(title,fontsize="small")
    plt.legend(fontsize="x-small")
    

def MutipleBarProp(excel='Arts.xlsx',start=0,end=3,title="Arabic and Archaeology CGPA Bar Chart"):
    data=CategorizeCgpa(excel)
    cgpaArray=[]
    Departmentlabel=list(data.keys())[start:end]
    X_axis1=np.arange(4+1)
    numbersOfDepartment=end-start
    k=len(Departmentlabel)
    for i in range(len(Departmentlabel)):
        label=Departmentlabel[i]
        width=0.94/numbersOfDepartment
        workingData=np.array(data[label][0])
        newData=workingData*100/sum(workingData)
        
        X_axis=np.arange(4+1)-(len(Departmentlabel)-1)/2*width
        #plt.bar(X_axis-0.08*(i+0.01)*(-1)**i,newData,0.23,label=label)
        plt.bar(X_axis+width*i,np.array(newData)+0.17,width,label=label)
    plt.xticks(X_axis1,["firstClass", "secondClassUpp", ". secondClassLow", "thirdClass", "withdrawn"],fontsize="5")
    #plt.xlabel("Category of Honour")
    plt.ylabel("Percentage of Students")
    plt.title(title,fontsize="small")
    plt.legend(fontsize="x-small")


def SixDeptPop():
    plt.subplot(2, 3, 1)
    MutipleBarProp(title='linguistic CGPA Bar Chart', excel='linguisticPhilosophy.xlsx', end=3,start=0)
    plt.subplot(2, 3, 2)
    MutipleBarProp(title='Philosophy CGPA Bar Chart', excel='linguisticPhilosophy.xlsx', end=6,start=3)
    plt.subplot(2, 3, 3)
    MutipleBarProp(title='Chemistry  CGPA Bar Chart', excel='ChemistComputer.xlsx', end=3,start=0)
    plt.subplot(2, 3, 4)
    MutipleBarProp(title='Computer CGPA Bar Chart', excel='ChemistComputer.xlsx', end=6,start=3)
    plt.subplot(2, 3, 5)
    MutipleBarProp(title='Arabic  CGPA Bar Chart', end=3,start=0)
    plt.subplot(2, 3, 6)
    MutipleBarProp(title='Archaeology CGPA Bar Chart', end=6,start=3)
    plt.show()


def SixDept():
    plt.subplot(2, 3, 1)
    MutipleBar(title='linguistic CGPA Bar Chart', excel='linguisticPhilosophy.xlsx', end=3,start=0)
    plt.subplot(2, 3, 2)
    MutipleBar(title='Philosophy CGPA Bar Chart', excel='linguisticPhilosophy.xlsx', end=6,start=3)
    plt.subplot(2, 3, 3)
    MutipleBar(title='Chemistry  CGPA Bar Chart', excel='ChemistComputer.xlsx', end=3,start=0)
    plt.subplot(2, 3, 4)
    MutipleBar(title='Computer CGPA Bar Chart', excel='ChemistComputer.xlsx', end=6,start=3)
    plt.subplot(2, 3, 5)
    MutipleBar(title='Arabic  CGPA Bar Chart', end=3,start=0)
    plt.subplot(2, 3, 6)
    MutipleBar(title='Archaeology CGPA Bar Chart', end=6,start=3)
    plt.show()
SixDept()
