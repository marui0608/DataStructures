'''
    汉诺塔问题
    相传在古印度圣庙中，有一种被称为汉诺塔(Hanoi)游戏。
    该游戏是在一块铜板装置上，有三根杆(编号A、B、C)，在A杆自下而上、由大到小按顺序防止64个金盘
    游戏的目标：把A杆上的金盘全部移到C杆上，并仍保持原有顺序叠好。
    操作规则：每次只能移动一个盘子，并且在移动过程中三根杆上都原本保持大盘在下，小盘在上，操作过程中盘子可以置于A、B、C任一杆上。

    递归三要素：
    1、最小条件：正确的在一个杆上，挪动一次盘子
    2、3个杆，第一次挪动的杆需要挪动剩余63个，然后继续挪动1次，还剩下62个，依次类推
    3、函数

    (1) 以C盘为中介，从A杆将1至n-1号盘移至B杆；
    (2) 将A杆中剩下的第n号盘移至C杆；
    (3) 以A杆为中介；从B杆将1至n-1号盘移至C杆。
    height:表示塔还剩多少层
'''
from pythonds.basic.stack import Stack
class Solution:
    def hanota(self,A,B,C):
        n = len(A)
        self.moveTower(n,A,B,C)

    def moveTower(self,n,A,B,C):
        if n == 1:
            C.append(A.pop())
            return
        else:
            self.moveTower(n-1,A,C,B)
            C.append(A.pop())
            self.moveTower(n-1,B,A,C)