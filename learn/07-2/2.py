# 347. 前 K 个高频元素
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
#
# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
# 示例 2:
# 输入: nums = [1], k = 1
# 输出: [1]
#
# 提示：
# 1 <= nums.length <= 105
# k 的取值范围是 [1, 数组中不相同的元素的个数]
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
#
# 进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。


from typing import List
from queue import PriorityQueue


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count_dict = {}
        # for i in nums:
        #     if i in count_dict:
        #         count_dict[i] += 1
        #     else:
        #         count_dict[i] = 1
        # sort_dict = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
        # count = 0
        # res = []
        # for i in sort_dict:
        #     res.append(i[0])
        #     count += 1
        #     if count == k:
        #         break
        # return res

        pass

        counts = {}
        for num in nums:
            count = counts.get(num, 0)
            counts[num] = count + 1
        queue = PriorityQueue(k)
        for key, value in counts.items():
            if queue.qsize() < k:
                queue.put([value, key])
            else:
                minVal, minKey = queue.get()
                if minVal < value:
                    queue.put([value, key])
                else:
                    queue.put([minVal, minKey])
        result = []
        for i in range(k):
            val, key = queue.get()
            result.append(key)
        return result


if __name__ == '__main__':
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    nums2 = [1]
    k2 = 1

    s = Solution()
    r1 = s.topKFrequent(nums1, k1)
    r2 = s.topKFrequent(nums2, k2)
    print(r1)
    print(r2)
