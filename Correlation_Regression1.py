Physics_Scores = list(map (int, ("15  12  8   8   7   7   7   6   5   3".split())))
History_Scores = list(map (int, ("10  25  17  11  13  17  20  13  9   15".split())))

def mean(someList):
    total = 0
    for a in someList:
        total += float(a)
    mean = total/len(someList)
    return mean
def standDev(someList):
    listMean = mean(someList)
    dev = 0.0
    for i in range(len(someList)):
        dev += (someList[i]-listMean)**2
    dev = dev**(1/2.0)
    return dev
def correlCo(someList1, someList2):

    xMean = mean(someList1)
    yMean = mean(someList2)
    xStandDev = standDev(someList1)
    yStandDev = standDev(someList2)

    rNum = 0.0
    for i in range(len(someList1)):
        rNum += (someList1[i]-xMean)*(someList2[i]-yMean)

    rDen = xStandDev * yStandDev

    r =  rNum/rDen
    return r

print(round(correlCo(Physics_Scores , History_Scores),3))