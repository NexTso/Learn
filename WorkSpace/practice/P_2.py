'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
'''
#請使用者輸入利潤(並轉為int格式)
Profit = int(input("please enter the Profit(I):"))

#此段支援自訂利潤獎金抽成參數
#設定參數:利潤分級
Grand = [0,100000,200000,400000,600000,1000000]
#設定參數:分級提成
Grand_Bonus = [0.1,0.075,0.05,0.03,0.015,0.01]
#分級段數
len_Grand = len(Grand)
#預設獎金為0
bonus = 0
#倒排利潤分級&分級提成
Grand=Grand[::-1]
Grand_Bonus=Grand_Bonus[::-1]

#依序判定利潤大小以及提成
for i in range(len_Grand) :
    if Profit > Grand[i] :
        bonus += (Profit-Grand[i])*Grand_Bonus[i]
        Profit = Grand[i]

#印出總獎金
print("The bonus is %i dollars." %bonus)

'''
#依序判定利潤大小以及提成
if Profit <= 0 :
    pass
elif Profit > Grand[-1] :
    for i in range(len_Grand-1) :
        bonus += int((Grand[i+1]-Grand[i]) * Grand_Bonus[i])     
    bonus = int( bonus + (Profit - Grand[-1]) * Grand_Bonus[-1])
elif Profit <= Grand[1] :
    bonus = int(Profit * Grand_Bonus[0])
else : 
    for j in range(2,len_Grand) :
        if Profit <= Grand[j] :
            for i in range(j-1) :
                bonus += int((Grand[i+1]-Grand[i]) * Grand_Bonus[i])
            bonus = int( bonus + (Profit - Grand[j-1]) * Grand_Bonus[j-1])
            break
        else :
            pass
#印出總獎金
print("The bonus is %i dollars." %bonus)
'''
