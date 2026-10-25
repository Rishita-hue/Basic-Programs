def Transpose_matrix (mat):
    A_Transpose=[]
    for i in range(len(mat[0])):
        row = []
        for j in range(len(mat)):
         row.append(mat[j][i])
        A_Transpose.append(row)
       
    return A_Transpose
mat= [
    [1,2],
    [3,4],
    [5,6],
] 
result_matrix = Transpose_matrix(mat)
print(result_matrix)