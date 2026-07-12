from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))  # Unique sorted elements
        rank = {}

        # Assign ranks
        for i, num in enumerate(sorted_arr, 1):
            rank[num] = i

        # Replace elements with their ranks
        return [rank[num] for num in arr]