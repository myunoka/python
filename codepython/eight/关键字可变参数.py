#关键字可变参数是用两个*星号表示
#还有注意的一点。不管是默认可变参数还是关键字可变参数都是可以调用空的，也就是调用时什么
#都不输入。程序返回的是空的元组或空的字典
def demo(**test): #可变参数输出是元组，关键字可变是输出字典
    for key,value in test.items(): #用for循环来输出两个字典里的key和value值
        print(key,':',value)
    print(test)
    print(type(test))
a = {'bj':'11c','gx':'32c'}
demo(**a)  #插入元组是一个星号 同样插入字典是两个星号