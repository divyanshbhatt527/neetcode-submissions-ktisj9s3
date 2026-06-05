class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # can't sort directly because the ord of indices will change
        new_nums = []
        for index,ele in enumerate(nums):
            new_nums.append((ele,index))

        new_nums.sort()
        i = 0
        j = len(new_nums) - 1

        while i<j:
            res = new_nums[i][0] + new_nums[j][0]
            if res == target:
                return [min(new_nums[i][1],new_nums[j][1]),
                max(new_nums[i][1],new_nums[j][1])]
            elif res > target:
                j -= 1
            else:
                i += 1
        