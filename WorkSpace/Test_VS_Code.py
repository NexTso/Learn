'''定義Car類別 和 Yugo子類別'''
class Car():
    def exlaime(self):
        print("I'm a Car!")
    def return_name(self,name):
        self.name = name
        print("My name is " + self.name)

class Yugo(Car):
    def exlaime(self):
        print("I'm a Car, Also a Yugo!")
    def number_name(self,name,number):
        super().return_name(name)
        self.number=number
        return [self.name,self.number]

'''指派thisCar給Car this Yugo給Yugo'''
thisCar=Car()
thisYugo=Yugo()

'''分別呼叫thisCar和thisYugo的exlaime func'''
thisCar.return_name("Toyota")
thisYugo.return_name("NASA")
print(thisYugo.number_name("KK",90))
