nums=[1,2,3,1]
n=len(nums)
for i in range(0,n):
    for j in range(1,n):
        if(nums[i]==nums[j]):
            print(True)
        else:
            print(False)