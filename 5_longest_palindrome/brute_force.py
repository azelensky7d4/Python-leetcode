class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        for left in range(len(s)):
            for right in range(left + 1, len(s) + 1):
                current_substring = s[left:right]
                if current_substring == current_substring[::-1] and len(current_substring) > len(longest_palindrome):
                    longest_palindrome = current_substring
        return longest_palindrome


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("abcba"))
    print(s.longestPalindrome("abc"))