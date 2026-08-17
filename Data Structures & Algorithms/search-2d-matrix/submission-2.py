class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        columns=len(matrix[0])
        req_row=-1
        
        for _ in range(rows):
            if target>=matrix[_][0] and target<=matrix[_][-1]:
                if matrix[_][0]==target or matrix[_][-1]==target:
                    return True
                req_row=_
                break

        if req_row==-1:
            return False
        
        left=0
        right=columns-1

        while left<=right:
            mid=(right+left)//2
            if matrix[req_row][mid]==target:
                return True
            elif matrix[req_row][mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False


        