from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        result = [item for item in arr if counts[item] == 1]
        if 1 <= k <= len(result):
            return result[k - 1]
        else:
            return ""