#######################################################################################################################
#                                          Author: Richie Magnotti
#
# Goal of code is to demonstrate sorting via quicksort algorithm
#######################################################################################################################

def QuickSort(A,lo,hi):
    if lo<hi:
        q = partition(A,lo,hi)
        QuickSort(A,lo,q-1)
        QuickSort(A,q+1,hi)

    print(A)

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

def main():
    arr1 = [2,9,13,4,2,5,24]
    p1 = 0
    r1 = len(arr1)-1
    #sending proper values
    QuickSort(arr1,p1,r1)



if __name__ == "__main__":
    main()

