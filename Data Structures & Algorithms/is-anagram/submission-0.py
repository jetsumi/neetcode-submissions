class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Lengths don't match
        if len(s) != len(t):
            return False
        # Check if the contents match
        return sorted(s) == sorted(t)