def bubbleSort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                    
    return arr

def time_bubble(lst):
	from timeit import default_timer as timer
	start = timer()
	bubbleSort(lst)
	finish = timer()
	print(finish - start)

#time_bubble([7,4,5,8,1,3])
