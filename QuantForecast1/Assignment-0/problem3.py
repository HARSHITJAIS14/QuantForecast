A=[[1,2,3],[4,5,6]]

def transpose(A):
    row=len(A)
    column=len(A[1])
    B=[]
    for i in range(column):
        B.insert(i,[])
    for i in range(len(B)):
        for j in range(row):
            B[i].insert(j,0)

    for i in range(row):
        for j in range(len(A[i])):
            B[j][i]=A[i][j]

    print(B)

transpose(A)

