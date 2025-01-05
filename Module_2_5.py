def get_matrix(n=2, m=3, value=15):
    matrix = []
    for i in range(n):
        matrix.append([])
        matrix_in = []
        for j in range(m):
            #исправить обращение к matrix
            matrix_in.append(value)
        matrix[i] = matrix_in
    return matrix

result0 = get_matrix()
result1 = get_matrix(2,2,10)
result2 = get_matrix(3,5,42)
result3 = get_matrix(4,2,113)

print(result0)
print(result1)
print(result2)
print(result3)
