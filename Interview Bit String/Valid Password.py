import re
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        A = "".join(A)
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

        # compiling regex
        pat = re.compile(reg)

        # searching regex
        mat = re.search(pat, A)

        # validating conditions
        if mat == True:
            return 1
        return 0

    # class Solution:
    # @param A : string
    # @return an integer
    def solve1(self, A):
        ans = 0

        if (len(A) < 8) or (len(A) > 15):
            return 0
        else:
            ans += 1

        if (" " in (A)):
            return 0

        else:
            arr1 = ['0', '1', '2', '3',
                    '4', '5', '6', '7', '8', '9']

        arr2 = ['@', '#', '!', '~', '$', '%', '^',
                '&', '*', '(', ',', '-', '+', '/',
                ':', '.', ',', '<', '>', '?', '|']

        for i in A:
            if i.isupper():
                ans += 1
                break

        for i in A:
            if i.isdigit():
                ans += 1
                break

        for i in A:
            if i.islower():
                ans += 1
                break

        for i in A:
            if i in arr2:
                ans += 1
                break
        # print(ans)
        if ans == 5:
            return 1
        else:
            return 0

ans = Solution()
A = ['S', 'c', 'a', 'l', 'e', 'r', '@', '1']
print(ans.solve(A))
