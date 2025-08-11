A =[[1,4,6],
    [4,6,9],
    [98,5,3]]

B=[[1,3,7,7],
   [5,8,3,2],
   [4,2,5,1]]

X =[[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            X[i][j]+= A[i][k]* B[k][j]
for i in X:
    print(i)





