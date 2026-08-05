class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #sliding window (fixed length slinding window)
        maxaverage=-1000000000
        left=0
        currentsum=0
        for right in range(len(nums)):
            currentsum+=nums[right]
            if right >= k-1:
                avg=currentsum/k
                maxaverage=max(avg,maxaverage)
                #leaving the value or subtracting the value
                currentsum -= nums[left]
                left+=1
        return maxaverage
                    