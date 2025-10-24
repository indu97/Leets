class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) < len(str2):
            small_str = str1
            big_str = str2
        else: 
            small_str = str2    
            big_str = str1
        
        m = len(small_str)
        n = len(big_str)

        key = small_str
        for j in range(m,0, -1):
            key = small_str[:j]
            for i in range(0,n,j):       
                if big_str[i:i+j]!= key:
                    break
            else:  # inner loop didn't break
                if small_str == key * (m // j):
                    return key
        return ""
                

        