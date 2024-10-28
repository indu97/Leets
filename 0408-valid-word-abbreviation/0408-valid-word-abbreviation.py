class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m = len(word)
        n = len(abbr)
        word_i = 0
        abbr_i = 0
        while (word_i < m and abbr_i < n):
            if abbr[abbr_i].isnumeric():
                # If leading zero, return False
                if abbr[abbr_i] == '0':
                    return False
                # If c is numeric, get the whole number
                num = ''
                for i in range(abbr_i, n):
                    if abbr[i].isnumeric():
                        num = num + abbr[i]
                    else:
                        break
                    abbr_i += 1

                # Advance the word ptr by num indices
                word_i += int(num)

                # # If word_i > end of word
                # if word_i > m:
                #     return False

            
            # If c is an alphabet
            elif abbr[abbr_i].isalpha():
                if word[word_i] != abbr[abbr_i]:
                    return False
                else:
                    word_i += 1
                    abbr_i += 1

        # If not end of word or abbr, return False
        return word_i == m and abbr_i == n

