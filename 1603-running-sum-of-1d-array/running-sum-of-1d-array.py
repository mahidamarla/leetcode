class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre=list(itertools.accumulate(nums))
        return pre
        