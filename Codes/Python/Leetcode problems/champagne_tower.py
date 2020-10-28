# Author: Sanket Dalvi
# Question Link: https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = []
        for i in range(1, query_row+2):
            tower.append([0]*i)
        tower[0][0] = poured
        for i in range(len(tower)-1):
            noOverflow = True
            for j in range(len(tower[i])):
                if tower[i][j] > 1:
                    noOverflow = False
                    tower[i+1][j] += (tower[i][j]-1)/2
                    tower[i+1][j+1] += (tower[i][j]-1)/2
                    tower[i][j] = 1
            if noOverflow: break
        return min(tower[query_row][query_glass], 1)

# Testing
print(Solution().champagneTower(1000000000, 29, 0))