"""
观察者模式是使用频率最高的设计模式之一，它用于建立一种对象与对象之间的依赖关系，一个对象发生改变时将自动通知其他对象，其他对象将相应作出反应。在观察者模式中，"发生改变的对象称为观察目标，而被通知的对象称为观察者"，一个观察目标可以对应多个观察者，而且这些观察者之间可以没有任何相互联系，可以根据需要增加和删除观察者，使得系统更易于扩展。
观察者模式定义如下： 观察者模式(Observer Pattern)：定义对象之间的一种一对多依赖关系，使得每当一个对象状态发生改变时，其相关依赖对象皆得到通知并被自动更新。观察者模式的别名包括发布-订阅（Publish/Subscribe）模式、模型-视图（Model/View）模式、源-监听器（Source/Listener）模式或从属者（Dependents）模式。观察者模式是一种对象行为型模式。
"""

from abc import ABCMeta, abstractmethod

# https://github.com/tylerlaberge/PyPattyrn#observer-pattern


class Observer(object, metaclass=ABCMeta):
    @abstractmethod
    def update(self, **state):
        """
        Abstract method that is called when an Observable's state changes.
        """
        pass


class Observable(object):

    def __init__(self):
        """
        Initialize a new Observable instance.
        """
        self._observers = set()

    def attach(self, observer):
        """
        Attach an observer to this Observable.

        @param observer: The Observer to attach.
        @type observer: Observer
        """
        self._observers.add(observer)

    def detach(self, observer):
        """
        Detach an observer from this Observable.

        @param observer: The Observer to detach.
        @type observer: Observer
        """
        try:
            self._observers.remove(observer)
        except KeyError:
            pass

    def notify(self):
        """
        Notify all attached Observers of the state of this Observable.
        """
        for observer in self._observers:
            state = {k: v for k, v in self.__dict__.items(
            ) if not k.startswith('__') and not k.startswith('_')}
            observer.update(**state)
