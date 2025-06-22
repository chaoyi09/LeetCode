class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_index = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            char = s[right]

            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right

            max_length = max(max_length, right - left + 1)

        return max_length