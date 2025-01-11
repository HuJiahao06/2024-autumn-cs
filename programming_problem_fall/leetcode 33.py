class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        for i in range(1,n):
            if nums[i]<nums[0]:
                new_nums=nums[i:]+nums[:i]
                k=i
                break
        else:
            k=0
            new_nums=nums[:]
        le,ri=0,n
        while le<ri:
            mid=(le+ri)//2
            if new_nums[mid]==target:
                return (k+mid)%n
            elif new_nums[mid]>target:
                ri=mid
            elif new_nums[mid]<target:
                le=mid+1
        return -1