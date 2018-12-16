"""
外观
*What is this pattern about?
The Facade pattern is a way to provide a simpler unified interface to
a more complex system. It provides an easier way to access functions
of the underlying system by providing a single entry point.
This kind of abstraction is seen in many real life situations. For
example, we can turn on a computer by just pressing a button, but in
fact there are many procedures and operations done when that happens
(e.g., loading programs from disk to memory). In this case, the button
serves as an unified interface to all the underlying procedures to
turn on a computer.
"""

'''
外观模式使用频率很高，它将其他很多对象整合在一起，提供给外界一个更简单的对象
'''


class Facade(object):
    pass
