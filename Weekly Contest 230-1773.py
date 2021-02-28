# https://leetcode.com/problems/count-items-matching-a-rule/


items, ruleKey,  ruleValue = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "type", "phone"



# items, ruleKey,  ruleValue = [["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"]], "name", "qqqq"



class Solution:
    def countMatches(self, items: list(list()), ruleKey: str, ruleValue: str) -> int:
        for i in zip(["type", "color", "name"], *items):
            if i[0] == ruleKey:
                return i.count(ruleValue)

solution = Solution()
print(solution.countMatches(items, ruleKey, ruleValue))

# Runtime: 244 ms, faster than 100.00% of Python3 online submissions for Count Items Matching a Rule.
# Memory Usage: 20.4 MB, less than 100.00% of Python3 online submissions for Count Items Matching a Rule.
