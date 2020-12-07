#Problem link: https://leetcode.com/problems/merge-sorted-array/

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        last, i, j = m + n - 1, m - 1, n - 1

        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[last] = A[i]
                last, i = last - 1, i - 1
            else:
                A[last] = B[j]
                last, j = last - 1, j - 1

        while j >= 0:
                A[last] = B[j]
                last, j = last - 1, j - 1
        return A

#Input:
#nums1 = [1,2,3,0,0,0], m = 3
#nums2 = [2,5,6],       n = 3

#Output: [1,2,2,3,5,6]

print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6],3))