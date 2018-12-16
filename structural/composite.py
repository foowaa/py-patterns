"""
组合
*What is this pattern about?
The composite pattern describes a group of objects that is treated the
same way as a single instance of the same type of object. The intent of
a composite is to "compose" objects into tree structures to represent
part-whole hierarchies. Implementing the composite pattern lets clients
treat individual objects and compositions uniformly.
"""

'''
组合模式必须有一个基类，这个基类是Composite里面的interface，基于这个基类还可以衍生出很多其他类。组合模式的意义在于，可以增添、删除 继承基类的对象和Composite对象，并可以一致性地处理所有对象（调用do_something()）
'''


class Composite(object):

    def __init__(self, interface):
        self.components = set()
        self.interface = interface

    def add_component(self, component):

        valid = False
        try:
            if component.interface == self.interface:
                valid = True
        except AttributeError:
            if self.interface in component.__class__.__mro__:
                valid = True
        finally:
            if valid:
                self.components.add(component)
            else:
                raise AttributeError('Component {0} does not follow this composites interface {1}'.format(
                    component.__class__, self.interface))

    def remove_component(self, component):

        try:
            self.components.remove(component)
        except KeyError:
            pass

    def _delegate(self, func_name):

        for component in self.components:
            attribute = getattr(component, func_name)
            if callable(attribute):
                attribute()
            else:
                raise AttributeError()

    def __getattr__(self, item):

        return lambda: self._delegate(item)
