"""
职责链模式
*What is this pattern about?
This pattern aims to decouple the senders of a request from its
receivers. It does this by allowing a request to move through chained
objects until it is handled by an appropriate receiver.

This is useful as it reduces the number of connections between objects,
since the sender does not need explicit knowledge of the handler, and
the receiver won't need to refer to all potential receivers, but keeps
a reference to a single successor.
"""

'''
“一对二”，“过”，“过”……这声音熟悉吗？你会想到什么？对！纸牌。在类似“斗地主”这样的纸牌游戏中，某人出牌给他的下家，下家看看手中的牌，如果要不起上家的牌则将出牌请求再转发给他的下家，其下家再进行判断。一个循环下来，如果其他人都要不起该牌，则最初的出牌者可以打出新的牌。在这个过程中，牌作为一个请求沿着一条链在传递，每一位纸牌的玩家都可以处理该请求。在设计模式中，我们也有一种专门用于处理这种请求链式传递的模式，它就是职责链模式。
'''

# see https://github.com/tylerlaberge/PyPattyrn#chain-of-responsibility-pattern
from abc import ABCMeta, abstractmethod

# set_successor(), handle()


class ChainLink(object, metaclass=ABCMeta):
    def __init__(self):
        """
        Initialize a new ChainLink instance.
        """
        self.successor = None

    def set_successor(self, successor):

        self.successor = successor

    def successor_handle(self, request):
        return self.successor.handle(request)

    @abstractmethod
    def handle(self, request):

        pass

# fail()


class Chain(object, metaclass=ABCMeta):

    def __init__(self, chainlink):

        self.chainlink = chainlink

    def handle(self, request):

        try:
            return self.chainlink.handle(request)
        except AttributeError:
            return self.fail()

    @abstractmethod
    def fail(self):
        pass
