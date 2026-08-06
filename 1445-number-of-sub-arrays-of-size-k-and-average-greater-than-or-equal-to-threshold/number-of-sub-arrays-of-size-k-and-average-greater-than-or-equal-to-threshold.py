class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target=k*threshold
        sub_sum=sum(arr[:k])
        count=0
        if sub_sum>=target:
            count+=1
        for i in range(k,len(arr)):
            sub_sum+=arr[i]
            sub_sum-=arr[i-k]
            if sub_sum>=target:
                count+=1
        return count