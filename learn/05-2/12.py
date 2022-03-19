# 349. 两个数组的交集
#
# 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
#
# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#
# 示例 2：
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 解释：[4,9] 也是可通过的
#
# 提示：
#     1 <= nums1.length, nums2.length <= 1000
#     0 <= nums1[i], nums2[i] <= 1000


from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1.sort()
        # nums2.sort()
        # l1, l2 = len(nums1), len(nums2)
        # result = []
        # i, j = 0, 0
        # while i < l1 and j < l2:
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #         continue
        #     if nums1[i] > nums2[j]:
        #         j += 1
        #         continue
        #     if nums1[i] not in result:
        #         result.append(nums1[i])
        #     i += 1
        #     j += 1
        # return result

        pass

        # temp_set = set()
        # for i in nums1:
        #     temp_set.add(i)
        # result = []
        # for j in nums2:
        #     if j in temp_set:
        #         temp_set.remove(j)
        #         result.append(j)
        # return result

        pass


if __name__ == '__main__':
    """一、k个数组求交集，两两求交集法
    两两求交集，组成新数组在和下一个数组两两求交集，循环调用
    """
    """二、k个数组求交集，多指针求交集法（k比较小的情况）
    比如三个数组求交集，先排序，再用三个指针，最小的前移一位，三个都相同了再一起前移一位
    要维护这三个指针的最小值，可以通过小顶堆进行实时维护（或者优先级队列）
    也可以通过hash表维护三个指针的值是否相等，在这三个值里面维护是否相等与最小值
    """
    """三、k个数组求交集，哈希表求交集法
    先排序，把每个数据存在hash表中，只能存一个（去重）
    第二个再把每个数据加一
    做完所有的
    值为k的就是交集
    """
    nums11 = [1, 2, 2, 1]
    nums12 = [2, 2]
    nums21 = [4, 9, 5]
    nums22 = [9, 4, 9, 8, 4]

    s = Solution()
    r1 = s.intersection(nums11, nums12)
    r2 = s.intersection(nums21, nums22)
    print(r1)
    print(r2)
