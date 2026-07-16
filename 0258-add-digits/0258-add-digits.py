class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=0
        n=0
        while num>=10:
            s=0
            while num>0:
                n=num%10
                s+=n
                num//=10
            num=s

        return(num)


        