class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        dict1 = {}

        for i in range(len(nums)):

            # Number needed to reach the target
            rem = target - nums[i]

            # If we've already seen it, we found the pair
            if rem in dict1:
                return [dict1[rem], i]

            # Store the current number and its index
            dict1[nums[i]] = i