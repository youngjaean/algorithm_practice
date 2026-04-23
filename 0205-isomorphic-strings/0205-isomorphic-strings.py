
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check_dict = {} 
        for i in range(len(s)):
            if s[i] in check_dict:
                if check_dict[s[i]] != t[i]:
                    return False
            elif t[i] in check_dict.values():
                return False
            check_dict[s[i]] = t[i]
        
        return True