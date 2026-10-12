class Solution:
    def isPalindrome(self, x: int) -> bool:
        test = str(x)
        l, r = 0,len(test)-1
        while l < len(test)//2+1:
            if test[l] != test[r]:
                return False
            l += 1
            r = len(test)-1-l
        return True