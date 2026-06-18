class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2, arr):
            i = j = k = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    arr[k] = arr1[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = arr2[j]
                    j += 1
                    k += 1
            while i < len(arr1):
                arr[k] = arr1[i]
                i += 1
                k += 1
            while j < len(arr2):
                arr[k] = arr2[j]
                j += 1
                k += 1

            return arr
        if len(nums) <= 1:
            return nums 
        mid = len(nums)//2
        arr1 = self.sortArray(nums[:mid])
        arr2 = self.sortArray(nums[mid:])

        result = merge(arr1, arr2, nums)

        return result