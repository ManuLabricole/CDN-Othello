from turtle import position
from case import Case

caseList = list()
def initCase():
    for i in range(8):
        for j in range(8):
            caseList.append(Case(position=(i,j), isFree=True, isPlayable=False))

initCase()
for i in caseList:
    print(i)

print(caseList)

