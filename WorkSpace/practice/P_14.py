'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''
from math import sqrt

num = int(input("請輸入一個正整數："))

def  factorization(num):
    #目前只有刪掉2的倍數，優化應要繼續刪掉3的倍數 5 的倍數.... 減少檢查量
    if num <=3 and num >0 :
        print(num)
    else:
        analysis = []
        checklist = list(range(3,int(sqrt(num))+1))
        checklist = checklist[::2]
        checklist.insert(0,2)
        for i in checklist : #檢查2以及比2大的奇數直至開根號數為止
            while num % i == 0 : #可除盡則繼續除
                analysis.append(i)
                num = num // i
        if num != 1 :  #如果剩下來的num仍未被除盡，則剩下的num比開根號大(且為質數)，直接印出。
            analysis.append(num)

    return analysis

answer = ""
for i in range(len(factorization(num))):
    answer += str(factorization(num)[i]) + "*"
print(answer[:-1])