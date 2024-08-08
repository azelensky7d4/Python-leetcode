class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_index = 0
        max_length = 0
        char_array = [-1] * 128
        for right_index, ch in enumerate(s):
            if char_array[ord(ch)] >= left_index:
                left_index = char_array[ord(ch)] + 1
            else:
                max_length = max(max_length, right_index - left_index + 1)
            char_array[ord(ch)] = right_index
        return max_length