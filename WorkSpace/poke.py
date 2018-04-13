import random as rd

class poke():
    def __init__(self,symbols,weight,games,product,extra,bet): #初始化預設戳戳樂固定屬性 局數 倍率 加場等
        self.symbol = [0,1,2] #三種圖標 0代表money 1代表乘倍(倍率由product參數提供) 2代表加場(場數由extra參數提供)
        self.symbols = []
        self.weight = []
        for i in range(len(self.symbol)) : 
            self.symbols.append(symbols[i]) #每個symbol的個數
            self.weight.append(weight[i])   #每個symbol的權重       
        self.initgames = games #初始可戳局數
        self.product = product #加倍倍數
        self.extra = extra #加局局數
        self.bet = bet #押注額
    
    def play(self): #進行遊戲
        count = self.initgames #可戳局數
        symbols = self.symbols.copy()
        weight = self.weight.copy()
        answer = [] #戳出的序列(初始化)
        Total_Weight = 0
        for i in self.symbol :
            Total_Weight += symbols[i]*weight[i] #總權重
        while count != 0 :
            count -= 1 #局數少1
            #print("Total_Weight = " + str(Total_Weight))
            seed = rd.randint(1,Total_Weight) #亂數取出本次種子
            #print("seed = "+ str(seed))
            check = 0 #檢查點
            for j in self.symbol: #依序檢查是不是戳到這個圖標
                check += symbols[j]*weight[j]
                if  seed <= check:
                    answer.append(j)
                    symbols[j] -= 1 #少一顆
                    Total_Weight -= weight[j] #總權重減少
                    #print(weight[j])
                    if j == 2 :
                        count += self.extra
                    break
        money = 0
        now_product = 1
        win = []
        for i in range(len(answer)) :
            if answer[i] == 0 :
                money = self.bet
            if answer[i] == 1 :
                now_product *= self.product
                money = 0
            elif answer[i] == 2 :
                money = 0
            win.append(now_product*(i+1)*money)    
        totalwin = sum(win)
        #print("戳戳樂結果為 : %s \n個別局數得分 : %s \n總贏分 : %s" %(answer,win,totalwin))
        return totalwin
        
slot_17 = poke([15,3,2],[18,10,20],5,2,3,1)
total = 0
for i in range(1000000):
    total += slot_17.play()
print("RTP = " + str(total/1000000))




