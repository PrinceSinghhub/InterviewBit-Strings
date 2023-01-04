class Solution:
    # @param A : string
    # @return an long
    def countSalutes(self, A):

        stack = []
        ans = 0

        for i in range(len(A)):
            if A[i] == '<':
                if len(stack) != 0 and stack[-1] == '>':
                    ans += len(stack)

            if A[i] == '>':
                stack.append('>')

        return ans
