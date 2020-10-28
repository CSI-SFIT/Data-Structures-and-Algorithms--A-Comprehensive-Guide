# Author: Sanket Dalvi
# Question Link: https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def __init__(self):
        super().__init__()
        self.ipList = []
    def getList(self, level, A, suffix):
        if level > 3:
            if len(suffix)-4 == len(A) and suffix[1:] not in self.ipList: 
                self.ipList.append(suffix[1:])
            return
        temp = []
        for i in range(1,min(4, len(A)+level-len(suffix)+1)):
            if 0 <= int(
                A[len(suffix)-(level):len(suffix)-level+i]) <= 255 and (
                    A[len(suffix)-(level):len(suffix)-level+i][0] != "0" or len(
                        A[len(suffix)-(level):len(suffix)-level+i]
                        ) == 1
                ):
                self.getList(level+1, A, suffix+"."+A[len(suffix)-(level):len(suffix)-level+i])

    def restoreIpAddresses(self, A):
        self.getList(0, A, "")
        return self.ipList
        
# Testing
print(Solution().restoreIpAddresses("0100100"))