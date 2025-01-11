class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        m,n=len(matrix[0]),len(matrix)
        while i<n and target>=matrix[i][-1]:
            if target==matrix[i][-1]:
                return True
            else:
                i+=1
        if i==n:
            return False
        left,right=0,m-1
        while left<right:
            tar=int((left+right)/2)
            if matrix[i][tar]==target:
                return True
            elif matrix[i][tar]>target:
                right=tar-1
            elif matrix[i][tar]<target:
                left=tar+1
        if left==right:
            if matrix[i][left]==target:
                return True
            else:
                return False
        return False