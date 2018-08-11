# This program computes the fibonacci sequence

def f():

    n=input("What is the nth fibonacci sequence you wish to find? ")

    sumold=1
    sum= 0
    
    for i in range(n):
        sum= sum + sumold
        sumold=sum - sumold
    print "Your nth fibonacci sequence is", sum


f()
