class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle==haystack:
                return 0
        for i in range(len(haystack)-len(needle)+1):
            
            if needle==haystack[i:len(needle)+i]:
                return i       
            
        return -1
s=Solution()
print(s.strStr("abc","c"))