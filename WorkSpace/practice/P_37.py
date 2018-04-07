'''
题目：对10个数进行排序。
'''
nums = []
for i in range(10) :
    nums.append(int(input("請輸入第%d個數 : " %(i+1))))

nums.sort()

'''
for j in range(10) :
        for k in range(j+1,10) :
            a,b = nums[j],nums[k]
            if a > b :
                 nums[j] = b
                 nums[k] = a
'''
print(nums)

