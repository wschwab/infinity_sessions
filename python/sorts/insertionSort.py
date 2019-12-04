def insertionSort(arr):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor

    return arr

def time_insert(lst):
        from timeit import default_timer as timer
        start = timer()
        insertionSort(lst)
        finish = timer()
        print(finish - start)

#time_insert([7,4,5,8,1,3])
