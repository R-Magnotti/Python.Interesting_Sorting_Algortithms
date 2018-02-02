#######################################################################################################################
#                                           Author: Richie Magnotti
# This code will run Bubble_Sort and Quick_Sort each for 10 seconds.
# The passed arrays to be sorted will be of size 500 and will increase by 100 with each iteration
# I have commented out the other TEST arrays that could be passed to the sort functions, and can be uncommented to test.
# I have also commented out the print statement for the contents of the arrays because they are so large, but can
# be uncommented for verification purposes.
#######################################################################################################################
import random
import sys
import time

#######################################################################################################################
# Selection Sort Algorithm
# params @list
#######################################################################################################################
def Quick_Sort(A,lo,hi):
    if lo<hi:
        q = partition(A,lo,hi)
        Quick_Sort(A,lo,q-1)
        Quick_Sort(A,q+1,hi)

    return A

def partition(A,low,high):
    pivot = A[high]
    i = low-1

    for j in range(low,high):
        if A[j]<=pivot:
            i=i+1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp

    temp = A[i + 1]
    A[i + 1] = A[high]
    A[high] = temp

    return (i+1)

def QSTime():
    A = []  # list to be filled with random arbitrary nums
    LoL = []  # list of lists to store each one to be filled
    size = 500  # initial list size
    qsTime = []  # list to be filled with execution times for MS
    ###################################################################################################################
    # loop until 60 seconds passes, each
    ###################################################################################################################
    j = 0
    start_time = time.time()
    print("QS")
    while (time.time() - start_time) < 10:
        for i in range(size):
            A.append(random.randint(0, 10)) #for smaller numbers
            # A.append(random.randint(0,1000)) #for larger numbers
            # A.append(random.randint(0, 1000000))  # for massive numbers
            # A.append(random.randint(-50, 50))  # for negative small numbers
            # A.append(random.randint(-5000, 5000))  # for negative larger numbers
            # A.append(random.randint(-5000000, 5000000))  # for negative massive numbers
            # A.append(random.randint(0))  # for all repeat numbers of no value
        LoL.append(A)
        st = time.time()  # new start time
        p1 = 0
        r1 = len(LoL[j]) - 1
        temp = Quick_Sort(LoL[j], p1, r1)  # runs quicksort on each list within the list
        qsTime.append(time.time() - st) # adds time difference to dictionary for later use
        print("data size ", size, "| time to compute ", qsTime[j])
        #print("Sorted List: ", temp)
        A = []  # zero out to be filed again
        size = size + 100
        j = j + 1
    print("---------------------------------------------------")

#######################################################################################################################
# Bubble Sort Algorithm
# params @list
#######################################################################################################################
def Bubble_Sort(arr):
    n = len(arr)

    #print("before", arr)

    for i in range(0, n):
        #print("i", i, "item", arr[i])
        for j in range(0,n-1):
            #print("j", j, "item", arr[j])
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

def BSTime():
    A = []  # list to be filled with random arbitrary nums
    LoL = []  # list of lists to store each one to be filled----------------add
    size = 500  # initial list size
    bsTime = []  # disctionary to be filled with execution times for MS
    ###################################################################################################################
    # loop until 60 seconds passes, each
    ###################################################################################################################
    start_time = time.time()
    j = 0
    print("BS")
    while (time.time() - start_time) < 10:
        for i in range(size):
            A.append(random.randint(0, 10)) #for smaller numbers
            # A.append(random.randint(0,1000)) #for larger numbers
            # A.append(random.randint(0, 1000000))  # for massive numbers
            # A.append(random.randint(-50, 50))  # for negative small numbers
            # A.append(random.randint(-5000, 5000))  # for negative larger numbers
            # A.append(random.randint(-5000000, 5000000))  # for negative massive numbers
            # A.append(random.randint(0))  # for all repeat numbers of no value
        LoL.append(A)
        st = time.time()  # new start time
        temp = Bubble_Sort(LoL[j])  # runs merge-sort on each list within the list
        bsTime.append(time.time() - st)  # adds time difference to dictionary for later use
        print("data size ", size, "| time to compute ", bsTime[j])
        #print("Sorted List: ", temp)
        A = []  # zero out to be filed again
        size = size + 100
        j = j + 1
def main():
    #to change recursion limit and prevent error
    sys.setrecursionlimit(1000000)
    ###################################################################################################################
    # selection sort calculate time
    ###################################################################################################################
    QSTime()
    ###################################################################################################################
    # bubble sort calculate time
    ###################################################################################################################
    BSTime()

main()