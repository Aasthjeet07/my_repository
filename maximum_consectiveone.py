nums = [9,1,4,5]
# def main(nums):
#     for i in nums:
#         if i == 1:
#             return i
#         i += 1

# print(main(nums))
        


def findMaxConsecutiveOnes(nums):
    count = 0
    for i in nums:
        if i == 1:
            count += i
            i +=1
    return count

print(findMaxConsecutiveOnes(nums))
