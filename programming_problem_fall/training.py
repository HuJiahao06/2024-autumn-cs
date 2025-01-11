nums=[4,5,6,7,0,1,2]
n=len(nums)
for i in range(1,n):
    if nums[i]<nums[0]:
        new_nums=nums[i:]+nums[:i]
        break
print(new_nums)