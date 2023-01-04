class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        # x = "IVXLCDM"
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        # print(d)
        ans = 0
        for i in range(len(A) - 1):
            if d[A[i]] < d[A[i + 1]]:
                ans -= d[A[i]]
            else:
                ans += d[A[i]]
        ans += d[A[len(A) - 1]]
        return ans

