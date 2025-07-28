#Moore voting algorithm
nums = [3,2,3]
n = len(nums)
me = 0
cnt = 1
for i in range(0,n-1):
    if nums[i] == nums[i+1]:
        cnt -=1
    else:
        me = nums[i]
        cnt -=1

print (me)