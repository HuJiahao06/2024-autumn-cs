class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        le,ri=0,n
        while le<ri:
            mid=(le+ri)//2
            if nums[mid]==target:
                max_t=min_t=mid
                for i in range(mid+1,n):
                    if nums[i]==target:
                        max_t=i
                    else:
                        break
                for i in range(mid-1,-1,-1):
                    if nums[i]==target:
                        min_t=i
                    else:
                        break
                return [min_t,max_t]
            elif nums[mid]>target:
                ri=mid
            elif nums[mid]<target:
                le=mid+1
        return [-1,-1]