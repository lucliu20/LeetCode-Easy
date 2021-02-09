# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

"""
Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
"""

letters, target = ["c", "f", "j"], "j"

# Binary Search
# Referring to the LeetCode Template II
# Find the first False: https://leetcode.com/problems/find-peak-element/discuss/788474/General-Binary-Search-Thought-Process-%3A-4-Templates
class Solution:
    def nextGreatestLetter(self, letters: list(), target: str) -> str:
        left, right = 0, len(letters)
        while left < right:
            mid = left + (right-left) // 2
            if target >= letters[mid]:
                left = mid + 1
            else:
                right = mid
        
        return letters[left] if left < len(letters) else letters[0]

solution = Solution()
print(solution.nextGreatestLetter(letters, target))

# Runtime: 104 ms, faster than 88.15% of Python3 online submissions for Find Smallest Letter Greater Than Target.
# Memory Usage: 14.4 MB, less than 67.83% of Python3 online submissions for Find Smallest Letter Greater Than Target.


