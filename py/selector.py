# select n diff numbers from min - max
def traceArr(arr, min, max, n):
    if n > 0:
        for i in range(min, max-n+2):
            arr1 = arr[:]
            arr1.append(i)
            traceArr(arr1, i+1, max, n-1)
    elif n == 0:
        print arr    

# Demo, select 5 diff numbers from 1-10
traceArr([], 1, 10, 5);  