class Solution(object):
    def longestPalindrome(self, s):
        if s == s[::-1]:
            return len(s)
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        print(d)
        sum1=0
        odd=1
        for i in d:
            if d[i]%2==0:
                sum1+=d[i]
            elif d[i]==1 and odd==1:
                sum1+=odd
                odd+=1
            elif (d[i]%2 != 0 and d[i]>2):
                if odd==1:
                    sum1+=d[i]
                    odd+=1
                else:
                    sum1+=(d[i]-1)
        return sum1