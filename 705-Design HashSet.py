# https://leetcode.com/problems/design-hashset/

"""
Example:
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)
"""

# TLE
# class MyHashSet:
# 
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.arr = []
# 
#     def add(self, key: int) -> None:
#         for i in range(len(self.arr)):
#             if self.arr[i] == key:
#                 return
#         self.arr.append(key)
# 
#     def remove(self, key: int) -> None:
#         for i in range(len(self.arr)):
#             if self.arr[i] == key:
#                 self.arr.remove(key)
#                 return
# 
#     def contains(self, key: int) -> bool:
#         """
#         Returns true if this set contains the specified element
#         """
#         for i in range(len(self.arr)):
#             if self.arr[i] == key:
#                 return True
#         return False


LENGTH = 1000000
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [None] * LENGTH

    def add(self, key: int) -> None:
        indice = self.hash(key)
        self.arr[indice] = key

    def remove(self, key: int) -> None:
        indice = self.hash(key)
        self.arr[indice] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        indice = self.hash(key)
        if self.arr[indice] == None:
            return False
        else:
            return True
    
    def hash(self, key):
        return key%LENGTH


hashSet = MyHashSet()

hashSet.add(1)   
hashSet.add(2)   
print(hashSet.contains(1))    # returns true
print(hashSet.contains(3))    # returns false (not found)
hashSet.add(2)          
print(hashSet.contains(2))    # returns true
hashSet.remove(2)          
print(hashSet.contains(2))    # returns false (already removed)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Runtime: 280 ms, faster than 36.44% of Python3 online submissions for Design HashSet.
# Memory Usage: 40.9 MB, less than 5.63% of Python3 online submissions for Design HashSet.

