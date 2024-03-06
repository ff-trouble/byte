# test_str = "hello,world"
# print(test_str[3:5])
# print(test_str[-1:-3:-1])
# while True:
#     try:
#         a = input()
#         listA = []
#         for i in (range(int(a))):
#             listA.append(int(input()))
#         setA = set(listA)
#         listC = list(setA)
#         listC.sort()
#         for O in listC:
#             print(O)
#     except:
#         break
# while True:
#     try:
#         n = input()  # 指定为N个数，输入
#         lst = []  # 指定一个空列表
#         for i in range(int(n)):  # 循环N次
#             lst.append(int(input()))  # 空集合中追加一个N个数中的某一个随机数
#         uniq = set(lst)  # 列表去重，但是会变成无序
#         lst = list(uniq)  # 集合转列表
#         lst.sort()  # 列表排序
#         for i in lst:
#             print(i)  # 打印列表
#     except:
#         break



# # 引入函数库
#
# import datetime as dt
#
# # 获取当前时间
#
# now_time = dt.datetime.now()
#
# # 输出时间
#
# print(now_time)
# import time
#
# timestamp = time.time()
# print(timestamp)
# my_list = [1, 2, 3]
# assert 4 in [1, 2, 3]
# print("Assertion passed")