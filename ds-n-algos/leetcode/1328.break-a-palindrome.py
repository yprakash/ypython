# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/819060009/
    # Greedy
    def breakPalindrome(self, palindrome: str) -> str:
        if not palindrome or len(palindrome) < 2:
            return ""

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        mid = len(palindrome) // 2 if len(palindrome) % 2 == 1 else 0

        for char in alphabet:
            for i, p in enumerate(palindrome):
                if mid and i == mid:
                    continue
                if char < p:
                    return palindrome[:i] + char + palindrome[i+1:]
                elif char > p:
                    i = len(palindrome) - 1 - i
                    return palindrome[:i] + char + palindrome[i+1:]

        return ""


if __name__ == "__main__":
    testcases = [
        "a",  # ""
        "aa",  # "ab"
        "aaa",  # "aab"
        "aaaa",  # "aaab"
        "abccba",  # "aaccba"
        "aba",  # "abb"
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.breakPalindrome(testcase))
