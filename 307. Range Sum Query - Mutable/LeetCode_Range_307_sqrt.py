import math

class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.__sumDecomp()
        
    def update(self, index, val):
        block_id = index//self.block_size
        self.block[block_id] = self.block[block_id] - self.nums[index] + val
        self.nums[index] = val

    def sumRange(self, left, right):
        sum = 0
        startBlock = left//self.block_size
        endBlock = right//self.block_size
        if startBlock == endBlock:
            for i in range(left,right + 1):
                sum += self.nums[i]
        else:
            for i in range(left, (startBlock+1) * self.block_size):
                sum += self.nums[i]
            for i in range(startBlock + 1, endBlock):
                sum += self.block[i]
            for i in range(endBlock * self.block_size, right + 1):
                sum += self.nums[i]
        return sum

    def __sumDecomp(self):
        self.block_size = int(len(self.nums)**0.5) 
        block_id = - 1
        self.block = [0]*len(self.nums)
        for i in range(len(self.nums)):
            if i % self.block_size == 0:
                block_id += 1
            self.block[block_id] += self.nums[i]


obj = NumArray([-1])
print(obj.sumRange(0,0))
obj.update(0,1)
print(obj.sumRange(0,0))

'''
obj = NumArray([3,7,8,5,1,2,5,4,10])
param_2 = obj.sumRange(1, 7)
print(param_2)
'''

'''
obj = NumArray([1,3,5])
param_2 = obj.sumRange(0,2)
print(param_2)
obj.update(1,2)
print(obj.sumRange(0, 2))
'''
