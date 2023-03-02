
class Solution:
    def compress(self, chars) -> int:
        i=0
        j=0
        count=0
        if len(chars)==1:
            return len(chars)
        else:
            while(j<len(chars)):
                if chars[i]==chars[j]:
                    count+=1
                else:
                    if count!=1:   
                        chars[i+1]=str(count)
                        count=0 
                        for i in range(i+2,j):
                            chars[i]='-1'
                        i=j
                        j-=1
                    else:
                        count=0
                        i=j
                        j-=1
                j+=1
            chars[i+2:j]=[]
            
            if count!=1:
                chars[i+1]=str(count)
            
            zero=chars.count('-1')
            for i in range(zero):
                chars.remove('-1')
            n=len(chars)
            i=0
            while(i<len(chars)):
                if len(chars[i])!=1:
                    num=str(chars[i])
                    temp=len(str(chars[i]))
                    chars.pop(i)
                    temp2=i
                    for j in range(temp):
                        chars.insert(temp2,num[j])
                        temp2+=1
                i+=1
           
            return len(chars)