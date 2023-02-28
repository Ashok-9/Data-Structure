class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        if ruleKey=='type':
            key=0
        elif ruleKey=='color':
            key=1
        elif ruleKey=='name':
            key=2
        for i in range(len(items)):
            if items[i][key]==ruleValue:
                count+=1
        return count