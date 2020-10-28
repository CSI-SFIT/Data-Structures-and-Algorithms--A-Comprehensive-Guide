# Author: Sanket Dalvi
# Question Link: https://leetcode.com/problems/max-points-on-a-line/

from collections import defaultdict
from fractions import Fraction
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, points):
        res = 0
        if len(points) <= 2:
            return len(points)
        for ind, i in enumerate(points):
            dp = defaultdict(int)
            maxPoint = 0
            duplicateCount = 0
            for j in points[:ind]+points[ind+1:]:
                if i[0] == j[0]:
                    m = -999
                    if i[1] == j[1]:
                        duplicateCount += 1
                        continue
                else:
                    m = Fraction(i[1]-j[1], i[0]-j[0])
                dp[m] += 1
                maxPoint = max(maxPoint, dp[m])
            res = max(res, maxPoint+1+duplicateCount)
        return res

# Testing
# Input: [[1,1],[1,1],[1,1],[2,2],[2,2],[1,2]]
# Expected output: 5
print(Solution().maxPoints([[1,1],[1,1],[1,1],[2,2],[2,2],[1,2]]))