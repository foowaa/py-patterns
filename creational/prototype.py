"""
原型
*What is this pattern about?
This patterns aims to reduce the number of classes required by an
application. Instead of relying on subclasses it creates objects by
copying a prototypical instance at run-time.

"""

'''
原型模式是维护一个关于方法的原型对象，新对象只用clone，并传入属性即可。
'''


class Prototype(object):

    value = 'default'

    def clone(self, **attrs):
        """Clone a prototype and update inner attributes dictionary"""
        # Python in Practice, Mark Summerfield
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj

    # prototype = Prototype()
    # d = prototype.clone()
    # a = prototype.clone(value='a-value', category='a')
    # b = prototype.clone(value='b-value', is_checked=True)
