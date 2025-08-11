A=[[1,2,7],
   [8,5,4]]

T= [[0,0],
    [0,0],
    [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i] = A[i][j]

# print("the transpose of matrix is",T)
for i in T:
     print("the transpose of matrix is", i)