"""
抽象工厂
What is this pattern about?

In Java and other languages, the Abstract Factory Pattern serves to provide an interface for
creating related/dependent objects without need to specify their
actual class.

The idea is to abstract the creation of objects depending on business
logic, platform choice, etc.

In Python, the interface we use is simply a callable, which is "builtin" interface
in Python, and in normal circumstances we can simply use the class itself as
that callable, because classes are first class objects in Python.
"""

'''
factory是一个“类”（不是实例），给AbstractFactory传递不同的类，就会产生不同的self.factory对象.

抽象工厂是为了给外部一个更加抽象的接口。例如：

Sunny软件公司欲开发一套界面皮肤库，可以对桌面软件进行界面美化。用户在使用时可以通过菜单来选择皮肤，不同的皮肤将提供视觉效果不同的按钮、文本框、组合框等界面元素。该皮肤库需要具备良好的灵活性和可扩展性，用户可以自由选择不同的皮肤，开发人员可以在不修改既有代码的基础上增加新的皮肤。为了更好的实现可扩展性，可以按照一定标准将界面元素分类，例如‘形状’，正方形、圆形和椭圆形分别构成了三个不同的产品等级结构，就可以使用‘抽象工厂实现’。
'''


class AbstractFactory(object):

    def __init__(self, factory=None):

        self.factory = factory

    def use_factory(self, a):
        """Creates and shows a pet using the abstract factory"""
        factory_instance = self.factory(a)
        # factory_instance 需要实现的行为
