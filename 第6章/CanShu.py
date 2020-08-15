def story(**kwds):
    return 'Once upon a time,there was a' \
            '{job} called {name}.'.format_map(kwds)

def power(x,y,*others):
    if others:
        print('Received redundant parameters:',others)
    return pow(x,y)

def interval(start,stop=None,step=1):
    'Imitates range() for step >0'
    #如果没有给参数stop指定值
    if stop is None:
        #就调整参数start和stop的值
        start,stop  =  0,start
    result = []
    i = start
    while i<stop:
        result.append(i)
        i+=step
    return result

print(story(job = 'king',name = 'Gumby'))
print(interval(3,7))