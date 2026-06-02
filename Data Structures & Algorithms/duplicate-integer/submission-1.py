class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for num in nums:
            # Duplicate
            if num in check:
                return True
            # Not duplicate
            check.add(num)
        return False