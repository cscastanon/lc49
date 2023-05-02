#Leetcode 49
#Group Anagram
# Diff: Medium
#Time Complexity: O(m*n)
#m => # strings given
#n => # avg length of each string
#Space Complex: O(26*n)
# 26 = 26 characters
#n => number of strings were given, were storing each string 

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return result.values()