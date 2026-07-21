class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')

        # Augment with '1' on both ends.
        t = '1' + s + '1'

        # Run-length encoding of t.
        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        best_gain = 0

        # For every internal 1-block surrounded by 0-blocks,
        # the net gain is the sum of the lengths of the adjacent
        # zero blocks.
        for k in range(1, len(runs) - 1):
            if (
                runs[k][0] == '1'
                and runs[k - 1][0] == '0'
                and runs[k + 1][0] == '0'
            ):
                best_gain = max(
                    best_gain,
                    runs[k - 1][1] + runs[k + 1][1]
                )

        return total_ones + best_gain