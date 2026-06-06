class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffix = [-1]*len(arr)
        for i in range(len(arr)-2,-1,-1):
            suffix[i] = max(suffix[i+1],arr[i+1])

        return suffix