class Solution:
    def trap(self, height: List[int]) -> int:
        cnt=0
        i,j=0,len(height)-1
        max_left,max_right=height[0],height[-1]
        while i<j:
            if max_left<=max_right:
                i+=1
                if height[i]>=max_left:
                    max_left=height[i]
                else:
                    cnt+=max_left-height[i]
            else:
                j-=1
                if height[j]>=max_right:
                    max_right=height[j]
                else:
                    cnt+=max_right-height[j]
        return cnt