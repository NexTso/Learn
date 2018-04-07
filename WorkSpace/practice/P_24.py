'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''
z=2
m=1
seq=[]
for i in range(20):
    seq.append(z/m)
    z,m = z+m , z
answer = 0
for j in seq :
    answer += j

print(answer)