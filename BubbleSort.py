#######################################################################################################################
#                                          Author: Richie Magnotti
#
# Goal of code is to demonstrate sorting via bubble sort algorithm
#######################################################################################################################

def bubble_sort(arr):
    n = len(arr)

    print("before", arr)

    for i in range(0, n):
        print("i", i, "item", arr[i])
        for j in range(0,n-1):
            print("j", j, "item", arr[j])
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    print("after", arr)

def main():
    A = [0,5,3,13,1,7,4,3,7,6,5,9,2,7]

    bubble_sort(A)

if __name__ == "__main__":
        main()
