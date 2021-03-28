# https://leetcode.com/problems/number-of-different-integers-in-a-string/
# My post:
# https://leetcode.com/problems/number-of-different-integers-in-a-string/discuss/1131868/Python-3-Explained-Intuitive

word = "a123bc34d8ef34"
# word = "leet1234code234"
# word = "a1b01c001"
# word = "0a0"


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        def removeZeros(string):
            while len(string) > 1 and string[0] == "0":
                string = string.replace("0", "")
            return string

        for char in word:
            if char.isalpha():
                word = word.replace(char, " ")
        mylist = [x for x in word.split(" ") if len(x) > 0]
        for i, num in enumerate(mylist):
            if num[0] == "0":
                mylist[i] = removeZeros(num)
        myset = set(mylist)
        return len(myset)

solution = Solution()
print(solution.numDifferentIntegers(word))

# Runtime: 44 ms
# Memory Usage: 14.3 MB

