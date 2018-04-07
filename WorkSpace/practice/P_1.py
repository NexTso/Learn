'''题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k) and (j != k):
                print(i,j,k)
                count += 1
            else:
                pass

print(count)

from scipy.special import comb, perm

print(perm(6,4))
print(comb(6,4)*perm(4,4))

from itertools import combinations,permutations
print(list(permutations(range(1,5),3)))