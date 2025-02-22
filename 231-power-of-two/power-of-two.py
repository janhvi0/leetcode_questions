# import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False

        if n==1:
            return True
        
        if n>0 and n&(n-1) == 0:
            return True
            
        return False









        # if n==1:
        #     return True
        # if math.sqrt(n)%2==0:
        #     return True
        # else:
        #     return False
