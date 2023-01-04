class Solution:
    # @param A : string
    # @return a list of strings
    def deserialize(self, A):

        ans = []

        temp = ''
        for i in A:
            if i.isalpha():
                temp += i
            else:

                if len(temp) != 0:
                    ans.append(temp)
                    temp = ""
        if len(temp) != 0:
            ans.append(temp)

        return ans



ans = Solution()
a = "mxxxzclaql10~omttepvukq10~sckhqgagqt10~miaufqvumh10~jndrqnllah10~wqlithzmfi10~oczafaqcrz10~lnubllvcsq10~rzngzhllmw10~ntpvbeyxnk10~"
print(ans.deserialize(a))