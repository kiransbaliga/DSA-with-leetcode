class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            small = sorted(nums1)
            big = sorted(nums2)
        else:
            small = sorted(nums2)
            big = sorted(nums1)
        i = j = 0
        res = []
        while i < len(small) and j < len(big):
            if small[i] == big[j]:
                res.append(small[i])
                i += 1
                j += 1
            elif small[i] < big[j]:
                i += 1
            else:
                j += 1
        return res