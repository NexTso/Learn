'''
题目：求100之内的素数。
'''

initlist = list(range(2,101))
answer = []

while len(initlist) != 0 :
    answer.append(initlist.pop(0))
    inter = initlist[:]
    for j in range(len(initlist)) :
        if initlist[j] % answer[-1] == 0 :
            inter.remove(initlist[j])
    initlist = inter

print(answer)
