'''
题目：求一个3*3矩阵主对角线元素之和。
'''
n = int(input("請輸入矩陣大小(n) : "))
matrix = []
for k in range(n*n):
    matrix.append(int(input("請輸入第%d個數字 : " %k)))

answer = 0
for i in range(n) :
    for j in range(n) :
        if i == j :
            answer += matrix[(i*n)+j]

print(answer)