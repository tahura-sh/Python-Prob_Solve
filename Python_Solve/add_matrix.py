A =[[1,4,5],
    [7,9,8],
    [4,7,4]]

B =[[1,4,5],
    [7,9,1],
    [3,7,2]]

result =[[0,0,0],
         [0,0,0,0],
         [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result [i][j]=A[i][j]+B[i][j]

for z in result:
    print(z)

