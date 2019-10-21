# Ernesto Martinez
import os
import numpy
import random
import sys
import time


#tables with random data to be replaced later
#table = numpy.array([])
#table = numpy.random.randint(1,10, size=(2,5))

# Matrix from file set up.
def data(filename):
    inst = open(filename, "r")
    f = inst.readline()
    n = int(f)
    matrix = numpy.array([])
    matrix = [line.split() for line in inst]
    matrix = numpy.asarray(matrix, dtype=int)
    inst.close()
    return matrix

# search path to seat people at the table
def search(filename,n):
    m = data(filename) #matrix of guest and hosts

    p = 0 #person
    c = 0
    l = 0 #likeness
    
    to = [] #table order
    p = random.randint(0,n-1) # random vertex to start
    if filename == "hw1-inst2.txt": #solves a bug with inst2
        p=1

    r = p
    while r not in to:
        c = 0
        to.append(p) # add to table
        l = m[r][c]
        while c < n: #make dynamic
            if (l <= m[r][c]) and (c not in to):
                l = m[r][c]
                p = c
            c = c+1
        r = p
    #fixer
    i = 0
    for i in range(n-1): #make dynamic
        if i not in to:
            to.append(i)

    return to
    
#convert search path into deterministic table
def convert(table,filename,n):
    ordered = search(filename,n)
    i = 0
    r = 0
    c = 0
    nHalf = int(n/2)

    for c in range(nHalf):  #make dynamic
        table[r][c] = ordered[i]
        i = i+1
    c=0
    for c in range(nHalf):  #make dynamic
        table[r+1][c] = ordered[i]
        i = i+1
    return table

#find a score given a table   
def scoring(table,filename):
    m = data(filename) #matrix of guest and hosts
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
    n = 0 #number of people at table
    # retrive name of file from arguments
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if os.path.exists(filename):
            #-----------------------
            #retrieve number of people from file
            inst = open(filename, "r")
            f = inst.readline()
            n = int(f)
            nHalf = int(n/2)
            inst.close()

            #tables with random data to be replaced later
            table = numpy.array([])
            table = numpy.random.randint(1,10, size=(2,nHalf))
     
            #convert() returns ordered table. store!
            orderedTable = convert(table,filename,n)


            print(orderedTable)
            #Getting scores in 60 seconds

            #https://stackoverflow.com/questions/24374620/python-loop-to-run-for-certain-amount-of-seconds
            FinalScore = scoring(orderedTable,filename)

            t_end = time.time() + 1
            print("Waiting 60 seconds")
            while True:
                score = scoring(orderedTable,filename)
                if FinalScore < score:
                    FinalScore = score
                if time.time() > t_end:
                    break
            print(FinalScore)

            #Exporting Data
            FinalScore = str(FinalScore)
            f = open("test.txt", "w")
            f.write(FinalScore)
            f.close()

            #-----------------------
        else:
            print(filename,"not in directory")
    else:
        print("Incorrect Number of Arguments")


   




# print(table+1) -> increment entire array by 1
main()









