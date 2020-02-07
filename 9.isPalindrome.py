class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x_rev = x[::-1]
        if x == x_rev:
            return True
        else:
            return False
