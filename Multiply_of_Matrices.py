# Program to calculate the multiply of two matrices
def multiply_matrix(mat1,mat2):
    if len(mat1[0]) != len(mat2):
     return "Matrices cant be multiply "
    result = []
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat2[0])):
            total = 0
            for k in range (len(mat2)):
             total += mat1[i][k] * mat2[k][j]
            row.append(total)
        result.append(row)
    return result
matrix1 = [
    [1,2,3],
    [4,5,6]
]
matrix2=[
    [7,8],
    [9,10],
    [11,12]
]
result_matrix = multiply_matrix(matrix1,matrix2)
if isinstance (result_matrix,str):
   print(result_matrix)
else:
    print("Multiply of matrices")
    for row in result_matrix:
        print(row)