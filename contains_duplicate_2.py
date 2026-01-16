def containsNearbyDuplicate( nums, k):
        last_visited = {}
        for i,num in enumerate(nums):
            if num in last_visited:
                if i - last_visited[num] <= k:
                    return True
            last_visited[num]=i
        return False

nums=[1,2,3,1]
k=int(input())
print(containsNearbyDuplicate(nums,k))
        