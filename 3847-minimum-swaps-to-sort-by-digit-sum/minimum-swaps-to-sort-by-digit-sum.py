class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Sorting by (digit sum, value) fixes where each element must end up; a permutation
        # made of c cycles needs len - c swaps.
        n = len(nums)
        order = sorted(range(n), key=lambda i: (sum(map(int, str(nums[i]))), nums[i]))
        seen = [False] * n
        cycles = 0
        for i in range(n):
            if seen[i]:
                continue
            cycles += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = order[j]
        return n - cycles