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
def matrix():
    inst = open("hw1-inst1.txt", "r")
    f = inst.readline()
    n = int(f)
    matrix = [line.split() for line in inst]
    matrix = numpy.asarray(matrix, dtype=int)
    #for row in matrix:
     #   print(row)
    inst.close()
    return n

table = numpy.random.randint(1,10, size=(2,5))

def matching(a,b):
    #if they both hosts or guests, then return 0
    # else return 1
    n = matrix()
    if(a <= (n/2) and b <(n/2)):
        return 0
    else:
        return 1




#print(table)
print(matching(1,10))








