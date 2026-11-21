class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort in alphabetical order, then they'll be equal to each other
        # but the time complexity will be m.nlogn

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())

        