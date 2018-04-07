'''
题目：暂停一秒输出。
'''
'''
分析:使用 time 模組的 sleep 函數
'''

import time #匯入整個time庫 呼叫內部函數:使用方式 time.函數名稱 ex. time.sleep(1)
from time import sleep #僅從 time 庫中匯入 sleep 函數作為這裡的函數，使用方式:直接 sleep

output=[1,2,3,4,5]

time.sleep(1) #暫停1秒

print(output)