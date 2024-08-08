class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left_center, right_center):
            while left_center >= 0 and right_center < len(s) and s[left_center] == s[right_center]:
                left_center -= 1
                right_center += 1
            return s[left_center + 1:right_center]

        longest_palindrome = s[0]
        for i in range(len(s) - 1):
            even = expand_from_center(i, i)
            odd = expand_from_center(i, i + 1)

            if len(even) > len(longest_palindrome):
                longest_palindrome = even
            if len(odd) > len(longest_palindrome):
                longest_palindrome = odd

        return longest_palindrome


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("abcba"))
    print(s.longestPalindrome("abc"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("ab"))
    print(s.longestPalindrome("aa"))