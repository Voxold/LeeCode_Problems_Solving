class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowel_positions = [i for i in range(len(s)) if s[i] in vowels]
        s_list = list(s)

        i, j = 0, len(vowel_positions) - 1
        while i < j:
            s_list[vowel_positions[i]], s_list[vowel_positions[j]] = s_list[vowel_positions[j]], s_list[vowel_positions[i]]
            i += 1
            j -= 1
        
        return ''.join(s_list)