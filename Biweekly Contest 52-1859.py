# https://leetcode.com/problems/sorting-the-sentence/


# s = "is2 sentence4 This1 a3" # "This is a sentence"
s = "Myself2 Me1 I4 and3" # "Me Myself and I"


class Solution:
    def sortSentence(self, s: str) -> str:
        mylist = s.split(" ")
        res = ["" for _ in range(len(mylist))]
        for i in range(len(mylist)):
            res[int(mylist[i][-1])-1] = mylist[i][:-1]
        return " ".join(res)




solution = Solution()
print(solution.sortSentence(s))

# Runtime: 28 ms
# Memory Usage: 14.4 MB

