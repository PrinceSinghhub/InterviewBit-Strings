class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    # strings at index 0 is not used
    # to make indexing simple
    # Please note we will add space after every word
    one = ["", "one-", "two-", "three-", "four-",
           "five-", "six-", "seven-", "eight-",
           "nine-", "ten-", "eleven-", "twelve-",
           "thirteen-", "fourteen-", "fifteen-",
           "sixteen-", "seventeen-", "eighteen-",
           "nineteen-"
           ]

    # strings at index 0 and 1 are not used to make array indexing simple
    ten = ["", "", "twenty-", "thirty-", "forty-",
           "fifty-", "sixty-", "seventy-", "eighty-",
           "ninety-"
           ]

    # n is 1- or 2-digit number
    def numToWords(self, n, s):
        res = ""
        # if n is more than 19, divide it
        if (n > 19):
            res = res + Solution.ten[n // 10] + Solution.one[n % 10]
        else:
            res = res + Solution.one[n]

        # if n is non-zero
        if (n):
            res = res + s

        return res

    # Function to print a given number in words
    def convertToWords(self, n):
        # stores word representation of given number n
        out = ""

        # handles digits at ten crore and crore places (if any)
        out += self.numToWords((n // 10000000), "crore-")

        # handles digits at ten lakh and lakh places (if any)
        out += self.numToWords(((n // 100000) % 100), "lakh-")

        # handles digits at thousands and tens thousands places (if any)
        out += self.numToWords(((n // 1000) % 100), "thousand-")

        # handles digit at hundreds places (if any)
        out += self.numToWords(((n // 100) % 10), "hundred-")

        # we need to add "and" if the number is more than hundred and contains digit at ten's or one's place
        if (n > 100 and n % 100):
            out += "and-"

        # handles digits at ones and tens places (if any)
        out += self.numToWords((n % 100), "")
        out = out[:-1]  # to remove the last trailing "-"
        return out

    def solve(self, A, B):
        n = (int)(A)
        y = self.convertToWords(n)

        if (y == B):
            return 1

        return 0
