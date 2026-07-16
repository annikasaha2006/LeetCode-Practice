class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag=0
        l=set()
        for i in nums:
            if i not in l:
                l.add(i)
                flag=0
            elif i in l:
                flag=1
                break
        if(flag==0):
            return False
        if(flag==1):
            return True

           
        