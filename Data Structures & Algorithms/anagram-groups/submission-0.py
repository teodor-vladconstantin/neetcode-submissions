class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = dict()

        for word in strs:
            freqArray = [0] * 26
            for litera in word:
                freqArray[ord(litera) - ord('a')] += 1
            key = tuple(freqArray)
            if key not in hash:
                hash[key] = []
            hash[key].append(word)

        return list(hash.values())
            