class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lst=[0]
        summ=0
        n=len(nums)
        for i in nums:
            summ+=i
            lst.append(summ)
        for i in range(n):
            left_sum=lst[i]
            right_sum=lst[n]-lst[i+1]
            if left_sum==right_sum:
                return i
        return -1
