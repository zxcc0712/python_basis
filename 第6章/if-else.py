# # name = input('what is your name?')
# # # if name.endswith('Gumby'):
# # #     print('hello Gumby')
# # #if else 语句，进行逻辑判断
# # # elif 是else if 的缩写
# # # # a = ord('s')
# # # # print(a)
# # name = ''
# # while not name:
# #     name = input('please enter your name:')
# #
# #
# # print('hello,{}' .format(name))
#for 循环迭代的是列表￿
# d = {'x':1,'y':2,'z':3}
# for key,value in d.items():
#
#     print(key,'corresponds to',value)
#并行迭代工具的内置函数zip，当序列的长度不同时，函数zip将在最短的序列用完后停止缝合
index = 0
# #1、index是索引值，代表着列表中第几个值
# strings = ['0','1','2','3','4','5','6','7','8','9']
# #strings是整个基础母列表字符串
# num = input('请输入数学（0-9）:')
# for string in strings:
#     if num in string:
#         strings[index] = 'abc'
#     index +=1
# print(strings)
# from  math import sqrt
# for n in range(99,0,-1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break
while True:
    word = input('please enter a word: ')
    if not word:break
    print('the world is ' ,word)
