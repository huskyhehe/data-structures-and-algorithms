# Question 1
# time: O(N * S)    N = len(strs)  S = sum(len(word) for word in words)
# space: O(N)

import collections


class Solution1:
    def group_anagrams(self, strs):
        count_map = collections.defaultdict(list)
        for word in strs:
            freqs = [0] * 26
            for ch in word:
                freqs[ord(ch) - ord('a')] += 1
            count_map[tuple(freqs)].append(word)

        res = list(count_map.values())
        return res
