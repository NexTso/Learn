'''
题目：暂停一秒输出，并格式化当前时间。
'''

import time

time.sleep(1)
now=time.time()
print(time.strftime("%Y-%m-%d %H:%M:%S"))