class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left = 0
        length = len(s)
        mx = 0
        for right in range(length):
            dic[s[right]] = dic.get(s[right],0) + 1
            while s[right] in dic and dic[s[right]] > 1:
                if dic[s[left]] == 1:
                    dic.pop(s[left])
                else:
                    dic[s[left]] -= 1
                left += 1
            mx = max(right - left + 1, mx)
        return mx