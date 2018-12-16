"""
配适器
*What is this pattern about?
The Adapter pattern provides a different interface for a class. We can
think about it as a cable adapter that allows you to charge a phone
somewhere that has outlets in a different shape. Following this idea,
the Adapter pattern is useful to integrate classes that couldn't be
integrated due to their incompatible interfaces.

"""

'''
配适器将不同的属性、方法配适到同一接口
'''


class Adapter(object):

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__


# def main():
#     '''
#     猫的meow和狗的bark方法配适到make_noise
#     '''
#     objects = []
#     dog = Dog()
#     objects.append(Adapter(dog, make_noise=dog.bark))
#     cat = Cat()
#     objects.append(Adapter(cat, make_noise=cat.meow))
