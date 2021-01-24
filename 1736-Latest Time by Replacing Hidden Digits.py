# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

"""
Example 1:
Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.

Example 2:
Input: time = "0?:3?"
Output: "09:39"

Example 3:
Input: time = "1?:22"
Output: "19:22"
"""

time = "2?:?0"
# time = "0?:3?"
# time = "1?:22"
# time = "??:3?"


class Solution:
    def maximumTime(self, time: str) -> str:
        s = set(("0","1","2","3"))
        for i in range(len(time)-1, -1, -1):
            if time[i] == "?":
                if i == 4:
                    time = time[:4] + "9"
                    t = "9"
                if i == 3:
                    time = time[:3] + "5" + time[-1]
                    t = "5"
                if i == 1:
                    if time[i-1] == "2" or time[i-1] == "?":
                        time = time[:1] + "3" + time[2:]
                        t = "3"
                    else:
                        time = time[:1] + "9" + time[2:]
                        t = "9"
                if i == 0:
                    if t in s:
                        time = "2" + time[1:]
                        t = "2"
                    else:
                        time = "1" + time[1:]
                        t = "1"
            elif time[i].isdigit():
                t = time[i]
        return time

# Runtime: 40 ms
# Memory Usage: 14.1 MB

