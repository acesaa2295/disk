class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always perform binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            px = (low + high) // 2
            py = (m + n + 1) // 2 - px

            max_left_x = float('-inf') if px == 0 else nums1[px - 1]
            min_right_x = float('inf') if px == m else nums1[px]

            max_left_y = float('-inf') if py == 0 else nums2[py - 1]
            min_right_y = float('inf') if py == n else nums2[py]

            # Correct partition found
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (m + n) % 2 == 0:
                    return (
                        max(max_left_x, max_left_y)
                        + min(min_right_x, min_right_y)
                    ) / 2
                else:
                    return max(max_left_x, max_left_y)

            elif max_left_x > min_right_y:
                high = px - 1
            else:
                low = px + 1
                