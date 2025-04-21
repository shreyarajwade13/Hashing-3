"""
Hashing approach --
TC - O(n)
SC - O(n) ==> since using set
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if s is None or len(s) <= 10: return []

        hset = set()
        rtnData = set()

        for i in range(len(s) - 9):
            sub = s[i:i + 10]

            if sub in hset:
                rtnData.add(sub)
            hset.add(sub)

        return list(rtnData)
