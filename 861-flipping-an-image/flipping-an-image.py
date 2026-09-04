class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        lst1=[]
        for i in image:
            s=i[::-1]
            lst=[]
            for j in s:
                if j==1:
                    lst.append(0)
                elif j==0:
                    lst.append(1)
            lst1.append(lst)
        return lst1