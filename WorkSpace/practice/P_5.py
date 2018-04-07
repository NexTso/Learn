'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''
answer=[]

for i in range(3):
    answer.append(int(input("please enter Integer %i." %i)))

answer.sort()

print(answer)