class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def permuteStrings(self, A, B):
        if (len(A) != len(B)):
            return 0

        if (set(A) == set(B)):
            return 1
        return 0
