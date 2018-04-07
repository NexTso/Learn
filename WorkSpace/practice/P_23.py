'''
印菱形星星
'''

high = int(input("請輸入高度(奇數):"))
mid = high//2 + 1 

for i in range(1,high+1):
    if i <= mid :
        k = i
    else :
        k = list(range(high))[2*mid-i] 
    x=(mid-k)*" "+2*(k-1)*"*"+"*"
    print(x)


