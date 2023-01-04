class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        dic={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        lis=[1000,900,500,400,100,90,50,40,10,9,5,4,1]

        ans=""
        for num in lis:
            if (A==0):
                return ans
            temp=A//num
            A=A%num
            for i in range (temp):
                ans+=dic[num]
        return ans

