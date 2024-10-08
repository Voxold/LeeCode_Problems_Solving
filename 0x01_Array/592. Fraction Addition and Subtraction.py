import re
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall('[+-]?\d+/\d+', expression)
        
        numerator, denominator = 0, 1
        
        for fraction in fractions:
            num, denom = map(int, fraction.split('/'))

            numerator = numerator * denom + num * denominator
            denominator *= denom

            gcd = math.gcd(numerator, denominator)
            numerator //= gcd
            denominator //= gcd
        
        if numerator == 0:
            return "0/1"
        
        return f"{numerator}/{denominator}"