#missing number 
#sol 1: using temp arr 
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        temp = list(range(n+1)) 
        for i in temp:
            if i not in nums:
                return i
            
#sol 2 : using difference 
def missing(nums):
    n = len(nums)
    a = n*(n+1)//2
    ans = 0
    for i in nums:
        ans = ans + i
    res = a - ans
    return res

print(missing([0,1,3]))

#using BIT WISE XOR

    
