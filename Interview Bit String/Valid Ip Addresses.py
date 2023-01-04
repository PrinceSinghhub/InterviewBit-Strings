class Solution:
    # @param A : string
    # @return a list of strings 0 1 2 3
    def is_valid(self, s):
        IP = s.split('.')
        for i in IP:
            if len(i)>0 and len(str(int(i)))!=len(i):
                return False
            elif int(i)<0 or int(i)>255:
                return False
        return True

    def restoreIpAddresses(self, A):
        if len(A)>12 or len(A)<4:
            return []
        res = []
        for i in range(1, len(A)-2):
            for j in range(i+1, len(A)-1):
                for k in range(j+1, len(A)):
                    s = A[:k]+"."+A[k:]
                    s = s[:j]+"."+s[j:]
                    s = s[:i]+"."+s[i:]
                    if self.is_valid(s):
                        res.append(s)
        return res
ans = Solution()
a = "25525511135"
print(ans.restoreIpAddresses(a))