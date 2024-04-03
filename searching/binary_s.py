# For binary search to work, the array should always be in a sorted order 

arr = [1,2,3,4,5,6,7,8,9]
target = 6

l, r = 0, len(arr)-1
while l<=r:
    m = (l+r)//2
    if target > arr[m]:
        l = m+1
    elif target < arr[m]:
        r = m-1
    else:
        print(m)
