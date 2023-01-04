class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if not haystack or not needle:
            return -1
        dividor = haystack.split(needle)
        if len(dividor[0]) == len(haystack):
            return -1
        else:
            return len(dividor[0])

ans = Solution()
print(ans.strStr("codexcoder","coder"))
