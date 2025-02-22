class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split()
        n=len(slist)
        l=0
        r=n-1
        while l<r:
            slist[l],slist[r]=slist[r],slist[l]
            l+=1
            r-=1
        # print(slist)
        s2 = " ".join(slist)
        # print(s2)
        return s2