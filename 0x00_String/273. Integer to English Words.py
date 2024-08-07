class Solution:
    def numberToWords(self, num: int) -> str:
        num_to_word = {
            0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
            18: "Eighteen", 19: "Nineteen", 20: "Twenty",
            30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty",
            70: "Seventy", 80: "Eighty", 90: "Ninety",
        }
        
        def number_to_words(num):
            if num in num_to_word:
                return num_to_word[num]
            
            elif num < 100:
                return num_to_word[num // 10 * 10] + " " + num_to_word[num % 10]
            
            elif num < 1000:
                if num % 100 == 0:
                    return num_to_word[num // 100] + " Hundred"
                else:
                    return num_to_word[num // 100] + " Hundred " + number_to_words(num % 100)
            
            elif num < 1000000:
                if num % 1000 == 0:
                    return number_to_words(num // 1000) + " Thousand"
                else:
                    return number_to_words(num // 1000) + " Thousand " + number_to_words(num % 1000)
            
            elif num < 1000000000:
                if num % 1000000 == 0:
                    return number_to_words(num // 1000000) + " Million"
                else:
                    return number_to_words(num // 1000000) + " Million " + number_to_words(num % 1000000)
            
            else:
                if num % 1000000000 == 0:
                    return number_to_words(num // 1000000000) + " Billion"
                else:
                    return number_to_words(num // 1000000000) + " Billion " + number_to_words(num % 1000000000)

        if num == 0:
            return "Zero"
        
        return number_to_words(num)
