#初始化数据结构的函数
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

#编写获取人员姓名的函数
def lookup(data,label,name):
    return data[label].get(name)

#将人员存储到数据结构中的函数
def store(data,full_name):
    #通过拆分full_name创建一个名为names的列表
    names = full_name.split()
    #如果names长度是2，就将中间名设置为空字符串
    if len(names)==2:names.insert(1,'')
    #将first,middle,last存储在元组labels中
    labels = 'first','middle','last'
    #使用zip函数将标签和对应的名字合并
    for label,name in zip(labels,names):
        #获取属于该标签的列表,为什么返回的是列表？
        #字典返回的值，不确定是否为列表还是字符串，因此可以是列表
        people = lookup(data,label,name)
        print(people)
        if people:
            #将full_name附加到该列表的末尾
            people.append(full_name)
        else:
            #插入一个新的列表
            data[label][name] =full_name

# myName= {}
# init(myName)
# store(myName, 'hello a sister')
# print(lookup(myName,'middle',''))
# print(myName)

#收集参数、分配参数
