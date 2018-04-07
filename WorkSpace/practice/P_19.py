'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''

answer=[]

for i in range(2,1001) :
    prepare = [1]
    for k in range(2,i):
        if i % k == 0:
            prepare.append(k)
    check = 0
    for j in prepare :
        check += j
    if i == check :
        answer.append(i)

print(answer)
