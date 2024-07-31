class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_1 = s.count('1')
        count_0 = s.count('0')
        result = '1' * (count_1 - 1) + '0' * count_0 + '1'
        
        return result