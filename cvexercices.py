from decimal import Decimal


def postCodes(strpc1,strpc2):
    pcStart = int(strpc1[0:2])*1000 + int(strpc1[3:6])
    pcStop = int(strpc2[0:2]) * 1000 + int(strpc2[3:6])
    postCodesList = []
    for pc in range(pcStart+1,pcStop):
        btwPostCode = str(int(pc/1000))+"-"+str(pc%1000)
        postCodesList.append(btwPostCode)

    return  postCodesList

def missingElements(inputList,n):
    inputSet = set(inputList)
    wholeSet = set(list(range(1,n+1)))
    return list(inputSet.symmetric_difference(wholeSet))


def generateConstList(start=2.0,end=5.5,step=0.5):
    outputList = []
    while start<end+step:
        outputList.append(Decimal(start))
        start+=step
        #print(Decimal(start))
    return outputList

#print(postCodes( "79-900","80-155"))
#print(missingElements([2,3,7,4,9], 10))
#print(generateConstList())