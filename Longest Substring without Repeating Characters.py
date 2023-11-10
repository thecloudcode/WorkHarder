from collections import defaultdict

def lengthOfLongestSubstring(self, s: str) -> int:
    d = defaultdict(lambda: 0)
    i = 0
    j = 0
    maxx = 0
    while (j < len(s) and i < len(s)):

        if d[s[j]] == 0:
            d[s[j]] += 1
            j += 1
        else:
            d[s[j]] += 1
            while (i <= j and d[s[j]] > 1):
                if s[j] == s[i]:
                    i += 1
                    d[s[j]] -= 1
                    break
                else:
                    i += 1
        maxx = max(maxx, j - i + 1)
    return maxx

lengthOfLongestSubstring()
