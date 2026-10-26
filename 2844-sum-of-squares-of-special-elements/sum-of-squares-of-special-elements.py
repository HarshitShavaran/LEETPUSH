class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        for i in range(n):
            if(n % (i+1) == 0):
                a = nums[i]
                ret += a*a
        return ret