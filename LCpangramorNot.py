from collections import Counter
class Solution:

    def checkIfPangram(self, sentence: str) -> bool:
        a=[chr(i) for i in range(ord('a'),ord('z')+1)]
        count=0
        for i in a:
            if i in sentence:
                count+=1
        if count==26:
            return True
        else:
            return False
s=Solution()
a="thequickbrownfoxjumpsoverthelazydog"
print(s.checkIfPangram(a))