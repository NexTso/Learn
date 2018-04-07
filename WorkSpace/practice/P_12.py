'''
題目:輸出所有101~200之間的質數。
'''
import math

nums = list(range(101,201)) #將101~200的生成式轉為串列
nums_odd=nums[::2] #跳過所有偶數(2以外的偶數都不是質數)，減少計算量
prime_number=[] #建好一個用來放質數的串列

for i in range(len(nums_odd)) :
    isPrime = True
    for j in list(range(3,int(math.sqrt(nums_odd[i]))+1))[::2] :  #只檢查開根號以下的奇數     
        if nums_odd[i] % j == 0 :
            isPrime = False
            break
    if isPrime == True :
        prime_number.append(nums_odd[i])

print(prime_number)
print(len(prime_number))



