class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left_index = 0
        current_window = set()
        for right_index in range(len(s)):
            if s[right_index] not in current_window:
                current_window.add(s[right_index])
                max_len = max(max_len, len(current_window))
            else:
                while s[right_index] in current_window:
                    current_window.remove(s[left_index])
                    left_index += 1
                current_window.add(s[right_index])
        return max_len

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))