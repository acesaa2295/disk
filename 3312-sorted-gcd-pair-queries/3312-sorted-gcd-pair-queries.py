class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # freq[x] = occurrences of x in nums
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # div_cnt[d] = how many numbers are divisible by d
        div_cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                div_cnt[d] += freq[multiple]

        # exact[d] = number of pairs with gcd exactly d
        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            c = div_cnt[d]
            total = c * (c - 1) // 2
            multiple = d * 2
            while multiple <= mx:
                total -= exact[multiple]
                multiple += d
            exact[d] = total

        # Prefix sums of pair counts in increasing gcd order.
        # pref[i] = number of gcd-pairs with value <= i
        pref = [0] * (mx + 1)
        for d in range(1, mx + 1):
            pref[d] = pref[d - 1] + exact[d]

        # For each query q (0-indexed), find smallest d with pref[d] > q
        ans = []
        for q in queries:
            ans.append(bisect_right(pref, q))
        return ans