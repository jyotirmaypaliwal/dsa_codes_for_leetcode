a = [[1,2,3],[4,5,6],[7,8,9]]
target = 4

for i in a:
    l, r = 0, len(i)-1
    while l<=r:
        m = (l+r)//2
        if target > i[m]:
            l = m+1
        elif target < i[m]:
            r = m-1
        else:
            print(True)
            break
