#Here we are applying insertion sort algorithm
arr = [1,2,8,9,5,4]
for i in range(1, len(arr)):
    j = i - 1
    while j >= 0 and arr[j] > arr[j+1]:
        arr[j] , arr[j+1] = arr[j+1], arr[j]
        j-=1

print(arr)

