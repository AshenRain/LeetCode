class NumArray:

    def __init__(self, nums):
        self.nums = nums
        #print(nums)
        self.sum_prefix = self.sumPrefix()

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        self.sumPrefix(index)

    def sumRange(self, left: int, right: int) -> int:
        sum = self.sum_prefix[right + 1] - self.sum_prefix[left]
        return sum

    def sumPrefix(self, index = -1):
        sum = [0]
        if index == -1:
            for i in range(len(self.nums)):
                sum.append(sum[i] + self.nums[i])
            return sum
        else:
            for i in range(index,len(self.nums)):
                self.sum_prefix[i + 1] = self.sum_prefix[i] + self.nums[i]


obj = NumArray([1,3,5])
param_2 = obj.sumRange(0, 2)
print(param_2)
obj.update(1,2)
print(obj.sumRange(0, 2))