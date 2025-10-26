class Solution:

    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        arr = list(s)
        l , r = 0, len(arr)-1

        while l < r:
            if arr[l] not in vowels:
                l += 1
            elif arr[r] not in vowels:
                r -= 1
            else:
                arr[r], arr[l] = arr[l], arr[r]
                l += 1
                r -= 1
        
        return "".join(arr)
        