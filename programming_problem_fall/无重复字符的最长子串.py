class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n<=1:
            return n
        else:
            max_l=0
            buffer=set()
            for i in range(n-1):
                buffer.add(s[i])
                for j in range(i+1,n):
                    if s[j] not in buffer:
                        buffer.add(s[j])
                        max_l=max(max_l,j+1-i)
                    else:
                        max_l=max(max_l,j-i)
                        buffer=set()
                        break
            return max_l
