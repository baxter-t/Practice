'''
        Insertion sort

        Best case time: O(n)
        Average case time: O(n^2)
        Worst case time: O(n^2)

        Space: 1
'''

test = [4,2,5,6,8,1,4,7,8,9,4]

def insertionSort(arr):
    sorted = 1
    
    while sorted < len(arr):
        element = arr[sorted]
        
        for x in range(sorted) :
            
