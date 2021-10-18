class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        '''
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        '''
        char = {}
        n = 0
        for word in strs:
            w = ['']*26
            for i in word:
                position = ord(i)-ord('a')
                w[position] += i
            s = "".join(w)
            if s not in char.keys():
                char[s] = [word]
            else:
                char[s].append(word)

        return list(char.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
print(s.groupAnagrams(["aaaaaaaaaab", "abbbbbbbbbb", "aaaaaaaaaab"]))


