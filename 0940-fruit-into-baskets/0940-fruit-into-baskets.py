class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count1 = count2 = 0
        type1 = type2 = -1
        max_total = 0
        total = 0
        left = right = 0
        while(left <= right and right < len(fruits)):
            # Can add right to first bucket
            if fruits[right] == type1 or type1 == -1:
                type1 = fruits[right]
                count1 += 1
                right += 1
                total += 1
            # Can add right to second bucket
            elif fruits[right] == type2 or type2 == -1:
                type2 = fruits[right]
                count2 += 1
                right += 1
                total += 1
            else:
                if fruits[left] == type1: 
                    # If bucket1 becomes empty, add right to bucket 1
                    if count1 == 1:
                        type1 = fruits[right]
                        right += 1
                        count1 = 1
                        total += 1
                    else:
                        count1 -= 1
                # Remove left and check if bucket2 empties
                elif fruits[left] == type2:
                    if count2 == 1:
                        type2 = fruits[right]
                        right += 1
                        count2 = 1
                        total += 1
                    else:
                        count2 -= 1
                else:
                    return max(total, max_total)
                # Remove left
                left += 1
                total -= 1
            max_total = max(total, max_total)
        return max(total, max_total)


