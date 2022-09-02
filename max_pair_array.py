class Solution:
    def numberOfPairs(self, n: List[int]) -> List[int]:
        c=0
        l=n.copy()
        k=len(l)
        for i in range(k):
            for j in n:
                if l[i]==j and n.count(j)>=2:
                    n.remove(j)
                    n.remove(j)
                    c+=1
                    break
        return [c,len(n)]
