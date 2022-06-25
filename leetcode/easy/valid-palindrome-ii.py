# author: yprakash
# https://leetcode.com/problems/valid-palindrome-ii
# https://leetcode.com/submissions/detail/692150706/

class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        chance = True
        l, r = 0, len(s) - 1

        while l < r and s[l] == s[r]:
            l += 1
            r -= 1

        return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)


sol = Solution()
print(sol.validPalindrome(""))
print(sol.validPalindrome("a"))
print(sol.validPalindrome("aa"))
print(sol.validPalindrome("ab"))
print(sol.validPalindrome("abc"))
print(sol.validPalindrome("abcb"))
print(sol.validPalindrome("abba"))
print(sol.validPalindrome("abcba"))
print(sol.validPalindrome("abccdba"))
print(sol.validPalindrome("raceacar"))
print(sol.validPalindrome("amanaplanacanalpanama"))
