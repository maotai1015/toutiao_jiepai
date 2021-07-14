a = [5,1,1,19,29,2,0,0, 3, 34,23]

def qsort(arry, low, high):
    left = low
    right = high
    key = arry[low]

    while low<high:
        while right >= key:
            right -= 1
        arry[low] = arry[right]
        while left < low:
            left += 1
        arry[high] = arry[left]
    arry[left] = key



