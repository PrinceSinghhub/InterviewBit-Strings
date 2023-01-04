# optimize code
class Solution:
    # @param A : string
    # @return an integer

    def isPaindrome(self, s):
        return s == s[::-1]

    def solve(self, A):
        n = len(A)
        start = 0
        end = n - 1
        while start <= end:
            if A[start] != A[end]:
                if self.isPaindrome(A[start + 1:end + 1]) or self.isPaindrome(A[start:end]):
                    return 1
                else:
                    return 0
            start += 1
            end -= 1

        return 1


# brutforce Approch
'''class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        arr = list(A)

        for i in range(len(arr)):
            temp = arr[i]
            arr.pop(i)

            strr = ''.join(arr)

            if strr == strr[::-1]:
                return 1

            else:
                arr.insert(i,temp)

        return 0'''

ans = Solution()
A = "abecbea"
print(ans.solve(A))