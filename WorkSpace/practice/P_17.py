'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''
import re

test_str = str(input("請輸入一行字符:"))

#正規表達式 要學。這是查的 多練才會。
total = len(test_str)
num = len(re.findall("\d",test_str))
en = len(re.findall("\w",test_str))-num+len(re.findall("_",test_str))
space = len(re.findall(" ",test_str))
other = total-num-en-space

print("英文字母數:%d 空格數:%d 數字數:%d 其他字符數:%d" %(en,space,num,other))

