"""
建造者
*What is this pattern about?
It decouples the creation of a complex object and its representation,
so that the same process can be reused to build objects from the same
family.
This is useful when you must separate the specification of an object
from its actual representation (generally for abstraction).

"""

'''
没有人买车会只买一个轮胎或者方向盘，大家买的都是一辆包含轮胎、方向盘和发动机等多个部件的完整汽车。如何将这些部件组装成一辆完整的汽车并返回给用户，这是建造者模式需要解决的问题。建造者模式又称为生成器模式，它是一种较为复杂、使用频率也相对较低的创建型模式。建造者模式为客户端返回的不是一个简单的产品，而是一个由多个部件组成的复杂产品。

Builder对象是一个抽象基类，它定义了step1, step2两个顺序操作，之后的对象需要继承Builder，并实现step1和step2
'''

# Abstract Building


class Builder(object):
    def __init__(self):
        self.step1()
        self.step2()

    def step1(self):
        raise NotImplementedError

    def step2(self):
        raise NotImplementedError


'''
# Concrete Buildings
class House(Builder):
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big'
'''
