class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindrome in the given string using the Manacher's algorithm.

        :param s: said string.
        :return: the longest found palindrome
        """
        def expand_from_center(self, s: str, i: int) -> int:
            """
            Expand from the current pointer index and find the longest possible palindrome
            from this point as the center.

            :param self: self.
            :param s: given string.
            :param i: pointer index.
            :return: wing length of the longest palindrome.
            """
            length = 0
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if left == right:
                    left -= 1
                    right += 1
                else:
                    left -= 1
                    right += 1
                    length += 1
            return length

        # Preprocessing
        new_str = "#" + "#".join(s) + "#"
        palindrome_lengths = [0 for i in new_str]

        # Actual algo
        center = 0
        right = 0
        max_length = 0
        max_length_index = 0
        for i in range(len(new_str)):
            if i < right:
                palindrome_lengths[i] = min(right - i, palindrome_lengths[2 * center - i])
            else:
                palindrome_lengths[i] = expand_from_center(self, new_str, i)
                center = i
                right = palindrome_lengths[i]
            if palindrome_lengths[i] > max_length:
                max_length = palindrome_lengths[i]
                max_length_index = i

        # Postprocessing
        return new_str[max_length_index - max_length:max_length_index + max_length + 1].replace("#", "")


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("abcba"))
    print(s.longestPalindrome("aaaaaaa"))
    print(s.longestPalindrome("abc"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("ab"))
    print(s.longestPalindrome("aa"))