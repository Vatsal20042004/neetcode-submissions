class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) <= len(nums2):
            min_arr = nums1
            max_arr = nums2
        else:
            min_arr = nums2
            max_arr = nums1

        total_len = len(min_arr) + len(max_arr)
        half = total_len // 2
        even = (total_len % 2 == 0)

        left = 0
        right = len(min_arr)

        while left <= right:
            num_min = (left + right) // 2
            num_max = half - num_min

            left_min = (
                min_arr[num_min - 1]
                if num_min > 0
                else float("-inf")
            )

            left_max = (
                max_arr[num_max - 1]
                if num_max > 0
                else float("-inf")
            )

            right_min = (
                min_arr[num_min]
                if num_min < len(min_arr)
                else float("inf")
            )

            right_max = (
                max_arr[num_max]
                if num_max < len(max_arr)
                else float("inf")
            )

            if left_min <= right_max and left_max <= right_min:

                if even:
                    return (
                        max(left_min, left_max)
                        + min(right_min, right_max)
                    ) / 2

                else:
                    return min(right_min, right_max)

            elif left_min > right_max:
                right = num_min - 1

            else:
                left = num_min + 1