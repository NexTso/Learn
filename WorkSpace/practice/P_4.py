'''题目：输入某年某月某日，判断这一天是这一年的第几天？'''
#輸入年月日做為判斷參數
year = int(input('year:\n'))
mounth = int(input('mounth:\n'))
date = int(input('date:\n'))

#預設的每月日數,list[0]=0
date_of_mounth = [0,31,28,31,30,31,30,31,31,30,31,30,31]

#計算之前的幾個月總共有幾天，閏年額外判斷
answer = sum(date_of_mounth[0:mounth])

#先判斷是否需要計算閏年(過了2月才要判斷)
if mounth >= 3 :

    #判斷400年閏年,100年不閏,4年一閏(按照順序判斷)
    if year % 400 == 0 :
        answer += 1
    elif year % 100 == 0 :
        pass
    elif year % 4 == 0 :
        answer += 1
    else :
        pass
else:
    pass

#最後加上本月第幾天
answer = answer + date
#印出答案
print("It is the %ith day." %answer)

