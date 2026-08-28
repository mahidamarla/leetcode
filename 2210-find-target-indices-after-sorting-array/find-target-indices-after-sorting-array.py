class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sor=sorted(nums)
        lst=[]
        for i in range(len(sor)):
            if sor[i]==target:
                lst.append(i)
        return lst
