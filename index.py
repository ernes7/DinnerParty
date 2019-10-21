import os
import numpy
import random

#tables with random data to be replaced later
table = numpy.array([])
table = numpy.random.randint(1,10, size=(2,5))

# Matrix from file set up.
def data():
    inst = open("hw1-inst1.txt", "r")
    f = inst.readline()
    n = int(f)
    matrix = numpy.array([])
    matrix = [line.split() for line in inst]
    matrix = numpy.asarray(matrix, dtype=int)
    inst.close()
    return matrix

# search path to seat people at the table
def search():
    m = data() #matrix of guest and hosts
    p = 0 #person
    c = 0
    l = 0 #likeness
    
    to = [] #table order
    p = random.randint(0,9) # random vertex to start
    r = p
    while r not in to:
        c = 0
        to.append(p) # add to table
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

    return to
    
#convert search path into deterministic table
def convert(table):
    ordered = search()
    i = 0
    r = 0
    c = 0
    for c in range(5):  #make dynamic
        table[r][c] = ordered[i]
        i = i+1
    for c in range(5):  #make dynamic
        table[r+1][c] = ordered[i]
        i = i+1
    return table

#find a score given a table   
def scoring(table):
    m = data() #matrix of guest and hosts
    r = 0 #rows
    c = 0 #columns
    s = 0 #score
    p = 0 #person

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
    
    return s

def main():
    # retrive name of file from arguments
    # store into a string

    #retrieve number of people from file
    #create random table

    # pass the string to convert(string,table) "which calls search(string) then data(string)"
    # matrix is created!

    #convert() returns ordered table. store!
    #pass table to scoring(table)

    #export score for file. 

    pass

print(scoring(convert(table)))










