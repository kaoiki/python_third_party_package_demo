'''
@auther     周道道
@date       2023-09-03
@descrption 展示icecream库的一些使用，pip install icecream，这个库提供了一个比Print更友好的命令行输出
'''

from icecream import ic

def addition_func(x, y):
    result = x + y
    ic(result)

def complex_func(x):
    intermediate = x * 2
    ic(x, intermediate)
    return intermediate **2

def exception_func():
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        ic(result, e)

if __name__ == '__main__':
    result = addition_func(5,10) # output: ic| result: 15
    result = complex_func(5) # output: ic| x: 5, intermediate: 10, result: 200
    exception_func() # output: ic| result: 0, e: ZeroDivisionError('division by zero')
    ic.configureOutput(prefix='DEBUG:', outputFunction=my_custom_logger) #自定义输出