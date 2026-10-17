class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)

        sorted_arr = sorted((get_digit_sum(x), x) for x in nums)
        

        target_pos = {val: i for i, (_, val) in enumerate(sorted_arr)}
        

        vis = [False] * n
        ans = n
        
        for i in range(n):
            if not vis[i]:
                ans -= 1
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = target_pos[nums[j]]
                    
        return ans