class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2, arr):
            i,j,k = 0,0,0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] > arr2[j]:
                    arr[k] = arr2[j]
                    j += 1
                    k += 1
                else:
                    arr[k] = arr1[i]
                    k += 1
                    i += 1 
            
            while i < len(arr1):
                arr[k] = arr1[i]
                k += 1
                i += 1
            
            while j < len(arr2):
                arr[k] = arr2[j]
                j += 1
                k += 1
            
            return arr
            

        def mergeSort(nums):
            if len(nums) == 0 or len(nums) == 1:
                return nums
            
            mid = len(nums)//2
            arr1 = nums[:mid]
            arr2 = nums[mid:]
            arr1 = mergeSort(arr1)
            arr2 = mergeSort(arr2)
            res = merge(arr1, arr2, nums)

            return res
        
        return mergeSort(nums)
