# 1st methode
class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        hash = [0] * 26
        for c in A:
            hash[ord(c) - 97] += 1
        return hash

class Solution1:
    # @param A : string
    # @return a list of integers
    def solve(self, A):

        mydic = {}
        for i in range(97, 123):
            mydic[chr(i)] = 0

        for i in A:
            mydic[i] += 1

        ans = []
        for i in mydic.values():
            ans.append(i)

        return ans

ans = Solution()
a = "adtlnfbrryjnvabnrajbkrpywncrksxtgbtiqtzjgzstqbqxhltmghjemxxbxnnizmgcybnjhxnmybtuvdarwqtszxghjnpvkvhk"
print(ans.solve(a))
