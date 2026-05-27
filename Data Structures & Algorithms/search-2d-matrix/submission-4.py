class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # getting the correct row:
        low = 0
        high = m-1
        while low<=high:
            mid = (low+high)//2
            if matrix[mid][-1] >= target:
                if  matrix[mid][-1] == target:
                    return True
                else:
                    high = mid - 1
            else:
                low = mid + 1

        if low < m:
            row = low
        else:
            return False
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
                
