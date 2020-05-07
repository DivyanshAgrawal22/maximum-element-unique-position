import numpy as np
N = int(input("Enter the size of the matrix: "))
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
ar = np.array(arr)
rows = len(ar)
cols = len(ar[0])
max_lst = []
k = []
for i in range(rows):
    maximum = 0
    jtemp = 0
    for j in range(cols):
        if ar[i][j] > maximum and j not in k:
            maximum = ar[i][j]
            jtemp = j
    k.append(jtemp)
    max_lst.append(maximum)
print (k)
print(max_lst)
