class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = Counter(nums)
        return any(count > 1 for count in freq.values())