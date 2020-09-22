'''
    递归：递归是一种解决问题的方法。
    它把问题分解为越来越下的子问题，直到问题的规模小到可以被简单直接解决。
    特征：通常为了达到分解问题的效果“递归过程要引入一个调用自身的函数”
    解决问题类型：
'''

'''
    使用递归，计算5个数的和

def list_sum(num_list):
    the_num = 0
    for i in num_list:
        the_num = the_num + i
    return the_num
print(list_sum([1,2,3,4,5]))
'''

'''
    禁止使用while或者for
    (((1+2)+3)+4)+5
    num_list[i]+num_list[i+1]
    list_sum(num_list) = first(num_list)+listSum(rest(num_list))

import time
num_list = [x for x in range(1,501)]
def list_sum1(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0]+list_sum1(num_list[1:])

def list_sum2(num_list):
    the_num = 0
    for i in num_list:
        the_num = the_num + i
    return the_num

# 递归算法
start_time1 = time.time()
for i in range(1001):
    list_sum1(num_list)
end_time1 = time.time()

print(end_time1 - start_time1)

start_time2 = time.time()
for i in range(1001):
    list_sum2([1,2,3,4,5])
end_time2 = time.time()

print(end_time2 - start_time2)
'''

'''
    递归三大算法
        1.递归算法必须有个结束条件
        2.递归算法必须改变的状态并且向着基本技术条件演进
        3.递归算法必须递归的调用自身
'''

'''
    计算某个数的阶乘  5! = 1*2*3*4*5
    0! = 1

def fact(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n*fact(n-1)

print(fact(1))
'''

'''
    将整数转换为任意进制表示的字符串形式
    十进制    二进制      八进制     十六进制
      7      00000111       7          7
      10     00001010      o12         A

7/2   商3余1  3/2  商1余1   1/2 余1
7/8 1
7/16 7
0-9ABCDEF

def to_str(n,base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base,base) + convert_string[n%base]

print(to_str(10,2))

'''

'''
    1. 写一个函数，接收一个字符串作为参数，并返回一个反向的新的字符串
    2. 使用递归判断回文字符串
'''


