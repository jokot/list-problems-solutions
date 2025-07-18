from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == k:
            return nums
        
        dic = self.counter(nums)
        buckets = self.bucket_sort(len(nums), dic)
        top = self.get_top(buckets, k)

        return top
    
    def get_top(self, buckets, k):
        top = []
        for b in buckets[::-1]:
            for e in b:
                top.append(e)
                if len(top) == k:
                    return top
    
    def counter(self, nums):
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        return count

    def bucket_sort(self, size, dic):
        buckets = [[] for _ in range(size+1)]

        for key, val in dic.items():
            buckets[val].append(key)

        return buckets