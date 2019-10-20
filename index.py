import os
import numpy

# pick a P = person. ( Host 1 for example)
# y = best score of P. y = index. X += y 
# jump to that Index and make it P. 
# now find biggest score of P(y) that has not been a P yet. 
# P(y) = index = y. X += y.
# Repeat

matrix = numpy.array([])
table = numpy.array([])



# Table set up with all 0's
def data():
    inst = open("hw1-inst1.txt", "r")
    f = inst.readline()
    n = int(f)
    matrix = [line.split() for line in inst]
    matrix = numpy.asarray(matrix, dtype=int)
    inst.close()
    return matrix

table = numpy.random.randint(1,10, size=(2,5))

def matching(a,b):
    #if they both hosts or guests, then return 0
    # else return 1
    n = 10
    if(a <= ((n/2)+1) and b <= ((n/2)+1)):
        return 0
    else:
        return 1


def scoring(table):
    m = data() #matrix of guest and hosts
    r = 0 #rows
    c = 0 #columns
    s = 0 #score
    p = 0 #person

    p = table[r][c]

    #top&bot
    if (table[r+1][c]):
        s = s + m[p][table[r+1][c]]
        s = s + m[table[r+1][c]][p]

    #right
    if(table[r][c+1]):
        s = s + m[p][table[r][c+1]]
        s = s + m[table[r][c+1]][p]
    
    print(s)


print(table)
scoring(table)










