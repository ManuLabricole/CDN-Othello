from turtle import position
from case import Case


def initCase():
    for i in range(8):
        for j in range(8):
            Case(position=(i, j))

initCase()