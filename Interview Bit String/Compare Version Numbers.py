class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        a=list(map(int,A.split('.')))
        x=len(a)
        b=list(map(int,B.split('.')))
        y=len(b)
        while(x>y):
            b.append(0)
            y+=1
        while(y>x):
            a.append(0)
            x+=1
        if a>b:
            return 1
        if a<b:
            return -1
        return 0

ans = Solution()
a = "sdlfjl.sdfjksdj.skdjks"
b = "sdlfjl.sdfjksdj.skdjks"
print(ans.compareVersion(a,b))
