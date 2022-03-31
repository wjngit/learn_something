# 拓扑排序Kahn算法
# 有n个任务，已知两两之间的依赖关系，找到一个执行序列，满足所有的依赖关系
# 入度表示一个任务依赖其他任务的数量
# link = {
#     "A": ["B"],
#     "B": ["D"],
#     "C": ["A", "B"]
# }
# count_data = {"A": 1, "B": 2, "C": 0, "D": 1}
#
# def func(link, count_data):
#     zero_data = [0] * len(count_data)

