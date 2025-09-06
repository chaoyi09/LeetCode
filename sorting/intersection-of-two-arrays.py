class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        s = set(nums1)
        ans = set()
        for x in nums2:
            if x in s:
                ans.add(x)
        return list(ans)