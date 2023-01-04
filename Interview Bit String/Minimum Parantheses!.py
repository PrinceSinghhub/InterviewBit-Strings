class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        stack = []

        for i in range(len(A)):

            if A[i] == '(' or len(stack) == 0:
                stack.append(A[i])

            elif stack[-1] == '(':
                stack.pop()

            else:
                stack.append(A[i])

        return len(stack)


ans = Solution()
A = "((("
print(ans.solve(A))