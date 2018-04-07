'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
init_high = 100.0000
total_distance = init_high / 1.0000000000000
last_jump = 0.00000000000

for i in range(10):
    init_high = init_high / 2
    total_distance += init_high*2

total_distance -= init_high*2

print("共經過 %d 米，第10次反彈 %d 米" %(total_distance,init_high))
    