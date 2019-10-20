import os
import numpy

table = numpy.array([])
table = numpy.random.randint(1,10, size=(2,5))

# Table set up with all 0's
def data():
    inst = open("hw1-inst1.txt", "r")
    f = inst.readline()
    n = int(f)
    matrix = numpy.array([])
    matrix = [line.split() for line in inst]
    matrix = numpy.asarray(matrix, dtype=int)
    inst.close()
    return matrix

def search(table):
    m = data() #matrix of guest and hosts
    p = 0 #person
    c = 0
    l = 0 #likeness
    
    to = [] #table order
    p = 6 # or random number to start
    r = p
    while r not in to:
        #l = m[r][c]
        c = 0
        to.append(p) # add to table
        #c = 0
        l = m[r][c]
        while c < 10: #make dynamic
            if (l <= m[r][c]) and (c not in to):
                l = m[r][c]
                p = c
            c = c+1
        r = p
    
    #fixer
    i = 0
    for i in range(9): #make dynamic
        if i not in to:
            to.append(i)

    print(to)
    print(table)
    

    
        


def scoring(table):
    m = data() #matrix of guest and hosts
    r = 0 #rows
    c = 0 #columns
    s = 0 #score
    p = 0 #person

    print(table)

    # Add up scores horizontally
    # 1<->2, 2<->3, 3<->4 ... etc
    for r in range(2):
        for c in range(4):  #make dynamic
            p = table[r][c]
            #right
            if table[r][c+1]:
                s = s + m[p][table[r][c+1]]
                s = s + m[table[r][c+1]][p]
            if p < 5 and table[r][c+1] >= 5:  #make dynamic
                s = s + 1

    # Add up scores vertically
    # 1<->(n/2)+1, 2<->(n/2)+2, 3<->(n/2)+3 ... etc
    for r in range(1):
        for c in range(5): #make dynamic
            p = table[r][c]
            if (table[r+1][c]):
                s = s + m[p][table[r+1][c]]
                s = s + m[table[r+1][c]][p]
            if p < 5 and table[r+1][c] >= 5:  #make dynamic
                s = s + 2

    #print(s)

print(data())
search(table)
#scoring(table)










