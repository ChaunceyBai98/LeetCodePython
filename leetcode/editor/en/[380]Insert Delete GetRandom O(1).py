# Implement the RandomizedSet class: 
# 
#  
#  RandomizedSet() Initializes the RandomizedSet object. 
#  bool insert(int val) Inserts an item val into the set if not present. 
# Returns true if the item was not present, false otherwise. 
#  bool remove(int val) Removes an item val from the set if present. Returns 
# true if the item was present, false otherwise. 
#  int getRandom() Returns a random element from the current set of elements (
# it's guaranteed that at least one element exists when this method is called). 
# Each element must have the same probability of being returned. 
#  
# 
#  You must implement the functions of the class such that each function works 
# in average O(1) time complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", 
# "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
# 
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was 
# inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now 
# contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 
# randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now 
# contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, 
# getRandom() will always return 2.
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= val <= 2³¹ - 1 
#  At most 2 * 10⁵ calls will be made to insert, remove, and getRandom. 
#  There will be at least one element in the data structure when getRandom is 
# called. 
#  
#  Related Topics Array Hash Table Math Design Randomized 👍 5445 👎 293
import random
from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class RandomizedSet:
    # 删除的时候，待删除元素与最后一个元素交换后pop()掉
    def __init__(self):
        self.dict = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.dict.keys():
            return False
        self.nums.append(val)
        self.dict.setdefault(val, len(self.nums) - 1)
        return True

    def remove(self, val: int) -> bool:
        index = self.dict.get(val)
        if index is not None:
            # 修改最后添加的元素的索引为要删除元素的索引
            self.dict[self.nums[len(self.nums) - 1]] = index
            # 换完了再删除酒没有破事了
            self.nums[len(self.nums) - 1], self.nums[index] = self.nums[index], self.nums[len(self.nums) - 1]
            self.nums.pop()
            self.dict.pop(val)
            return True
        else:
            return False

    #     自己写的，没用交换，很复杂，还不对
    # def remove(self, val: int) -> bool:
    #     index = self.dict.get(val)
    #     if index is not None:
    #         if len(self.nums) == 1:
    #             self.nums.clear()
    #             self.dict.clear()
    #         elif(index == len(self.nums)-1):
    #             self.nums.pop()
    #             self.dict.pop(val)
    #         else:
    #             self.nums[index] = self.nums[-1]
    #             self.nums.pop()
    #             self.dict.setdefault(self.nums[-1], index)
    #             self.dict.pop(val)
    #         return True
    #     else:
    #         return False
    def getRandom(self) -> int:
        idx = random.randint(0, len(self.nums) - 1)
        # 返回该索引对应的元素
        return self.nums[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = RandomizedSet()
    print(a.insert(1))
    print(a.remove(2))
    print(a.insert(2))
    print(a.remove(1))
    print(a.insert(2))
