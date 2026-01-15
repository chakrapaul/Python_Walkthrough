def twoSum(nums:list[int],target):
    hash={}
    for i,num in enumerate(nums):
        diff = target - num
        if diff in hash:
            return[hash[diff],i]
        hash[num]=i


nums=[2,7,11,15]
target = 9
print(twoSum(nums,target))
