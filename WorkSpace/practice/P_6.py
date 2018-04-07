'''
斐波那契数列
'''
#輸入值
x=input("請輸入第幾個費波那契數列值.\n")

#製作費波那契數列(不使用遞迴以提升效率)
def febn(ith):
    answer=[0,1]

    if ith < 2 and ith >=0 :
        return answer(ith)
    elif ith >=2 :
        for i in range(ith - 1) :
            answer.reverse()
            answer[1] = answer[0] + answer[1]
        return answer[1]
    else :
        pass

#印出答案
print(febn(x))

'''
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

print(fib(x))
'''