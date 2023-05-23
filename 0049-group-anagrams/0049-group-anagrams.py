class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            s_string = str(sorted(string))
            if s_string in hashmap:
                hashmap[s_string].append(string)
            else:
                hashmap[s_string] = [string]

        return list(hashmap.values())