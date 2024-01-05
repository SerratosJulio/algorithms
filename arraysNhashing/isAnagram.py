class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dict1, dict2 = {}, {}

        for i in s:
            if i in dict1.keys():
                dict1[i] += 1
            else:
                dict1[i] = 1 
        
        for x in t:
            if x in dict2.keys():
                dict2[x] += 1
            else:
                dict2[x] = 1
        
        #validate each item in both dictionaries

        for key in dict1:
            if dict1[key] != dict2.get(key, 0):
                return False
        return True
