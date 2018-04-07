'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''

a = str(input("請輸入a值(1~9):"))
n = int(input("請輸入要連加幾次:"))
answer = 0
k=a[0]

for i in range(1,n+1) :
    answer += int(k)
    k += a
print(answer)

