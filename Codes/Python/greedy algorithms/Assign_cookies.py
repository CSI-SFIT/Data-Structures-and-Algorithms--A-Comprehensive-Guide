#Problem link : https://leetcode.com/problems/assign-cookies
#Leetcode Problem.455 : Assign Cookies


class Solution:
    def findContentChildren(g, s):
    #sort both (children and cookies list) in ascending order
        g.sort()
        s.sort()
        i = 0
        j = 0
        count = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1

        return count
    # g = [1,2], s = [1,2,3]

    # test the code
    if __name__ == "__main__":
       print(findContentChildren([1,2], [1,2,3]))



