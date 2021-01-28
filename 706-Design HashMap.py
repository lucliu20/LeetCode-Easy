# https://leetcode.com/problems/design-hashmap/

"""
Example:
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 
"""

LENGTH = 1000000
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [None]*LENGTH

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        indice = self.hash(key)
        self.arr[indice] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        indice = self.hash(key)
        if self.arr[indice] != None:
            return self.arr[indice]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        indice = self.hash(key)
        if self.arr[indice] != None:
            self.arr[indice] = None
    
    def hash(self, key):
        return key%LENGTH

hashMap = MyHashMap()

hashMap.put(1, 1)          
hashMap.put(2, 2)         
print(hashMap.get(1))            # returns 1
print(hashMap.get(3))            # returns -1 (not found)
hashMap.put(2, 1)          # update the existing value
print(hashMap.get(2))            # returns 1 
hashMap.remove(2)          # remove the mapping for 2
print(hashMap.get(2))            # returns -1 (not found) 
pass


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Runtime: 364 ms, faster than 28.65% of Python3 online submissions for Design HashMap.
# Memory Usage: 39.5 MB, less than 7.69% of Python3 online submissions for Design HashMap.


