class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        flag=0
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in sentence :
                flag=1
            else :
                flag=0
                break
        if flag==1:
            return True
        else :
            return False