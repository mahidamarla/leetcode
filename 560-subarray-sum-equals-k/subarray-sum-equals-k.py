class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        csum=0
        subcnt=0
        seen={0:1}
        for i in nums:
            #compute prefix sum
            csum+=i
            #required prefix sum(prefix(l-1),history)
            req=csum-k
            if req in seen:
                subcnt+=seen[req]
            seen[csum]=seen.get(csum,0)+1
        return subcnt
