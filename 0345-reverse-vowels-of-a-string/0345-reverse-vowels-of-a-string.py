class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        vowels={'a', 'e', 'i', 'o','u','A', 'E', 'I', 'O','U'}
        temp=''
        new=list(s)
        while i<j:
            if new[i] in vowels:
                pass
            else:
                i+=1

            if new[j] in vowels:
                pass
            else:
                j-=1

            if new[i] in vowels and new[j] in vowels:
                temp=new[i]
                new[i]=new[j]
                new[j]=temp
                i+=1
                j-=1
        s=''.join(new)       
        return s