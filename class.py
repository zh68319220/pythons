#!/usr/bin/env python
# encoding: utf-8
'''
class.py
python 类
python 2.7.x
'''

class Specialty(object):
    def __init__(self, spe):
        self.spe = spe

class People(object):
    def __init__(self, name):
        # 构造函数
        self.name = name

class Worker(People):
    def __init__(self, name, work):
        self.work = work
        # People.__init__(self, name)
        super(Worker, self).__init__(name)

    def say(self):
        print self.name
        print self.work

# 多重继承
class Fsd(Specialty, Worker):
    def __init__(self, name, work, position, spe):
        self.position = position
        Worker.__init__(self, name, work)
        Specialty.__init__(self, spe)

    def say(self):
        print self.name + ' ' + self.work + ' ' + str(self.position) + ' ' + self.spe

# 主程序入口
if __name__ == '__main__':
    w = Worker('yf', 'fsd')
    w.say()

    # 多重继承
    f = Fsd('yf', 'fsd', 123, 'front')
    f.say()

    print Fsd.__bases__
    print Fsd.__basicsize__