#Problem link: https://leetcode.com/problems/is-subsequence/
#Problem 392: Is Subsequence

class Solution:
    def isSubsequence(s, t):
        i=0
        #length of substring is 0 then  True by-default
        if len(s)==0:
         return True

        #loop through the main string and check for each element in substring
        for _ in range(len(t)):
         if t[_]==s[i]:
          i+=1
         if i==len(s):
           return True
        return False


    #test the code
    if __name__ == "__main__":
        print(isSubsequence('nge', 'nnghte'))


