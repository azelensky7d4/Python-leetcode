class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 1
        for index in range(len(s)):
            current = "" + s[index]
            if index == len(s) - 1:
                break
            for next_letter in s[index + 1:]:
                if next_letter not in current:
                    current += next_letter
                    if len(current) > max_len:
                        max_len = len(current)
                        max_string = current
                else:
                    break
        return max_len

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 3, abc
    print(s.lengthOfLongestSubstring("bb"))  # 1, b
    print(s.lengthOfLongestSubstring("pwwkew"))  # 3, wke
