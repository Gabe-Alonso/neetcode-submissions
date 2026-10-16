class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            letters = [0] * 26
            for j in range(len(strs[i])):
                letters[ord(strs[i][j]) - ord('a')] += 1
            count = tuple(letters)
            if count in groups:
                groups[count].append(strs[i])
            else:
                groups[count] = [strs[i]]

        return list(groups.values())