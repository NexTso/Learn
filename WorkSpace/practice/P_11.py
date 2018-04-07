'''
题目：古典问题：有一对兔子，
从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''
#輸入一個月份，列表至該月份
mounth=int(input("請輸入一個月份:\n"))

rm_1,rm_2,rm_3=2,0,0 #初始兔子數量,只有rm_3的兔子才會生小兔子
rabbits_list = [2]
if mounth == 1 :
    pass
else :
    for i in range(2,mounth+1):
        rm_1,rm_2,rm_3=int((rm_2+rm_3)//2)*2,rm_1,rm_3+rm_2
        rabbits_list.append(rm_1+rm_2+rm_3)

print('第%d個月兔子總數為 : %d' %(mounth,rabbits_list[-1]))

