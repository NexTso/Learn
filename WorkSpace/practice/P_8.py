'''
题目：输出 9*9 乘法表。
'''

for i in range(1,10) :
    ans=""
    for j in range(1,10):
        ans += "%ix%i=%i " %(i,j,i*j)
    print(ans)