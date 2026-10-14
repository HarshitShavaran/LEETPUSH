class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: 
            return ""
        s = str(s)
        start, max_len = 0, 0
        n = len(s)

        for i in range(n): 
            for left, right in ((i, i), (i, i + 1)):
                while left >= 0 and right < n and s[left] == s[right]: 
                    left -= 1
                    right += 1
                current_len = right - left - 1

                if current_len > max_len: 
                    start = left + 1
                    max_len = current_len
        return s[start: start + max_len]