"""
备忘录模式 
提供了一种状态恢复的实现机制，使得用户可以方便地回到一个特定的历史步骤，当新的状态无效或者存在问题时，可以使用暂时存储起来的备忘录将状态复原，当前很多软件都提供了撤销(Undo)操作，其中就使用了备忘录模式。
"""

# See: https://github.com/tylerlaberge/PyPattyrn#memento-pattern

from copy import deepcopy


class Memento(object):
    """
    Memento class as part of the Memento design pattern.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#memento-pattern}
    - External Memento Pattern documentation: U{https://en.wikipedia.org/wiki/Memento_pattern}
    """

    def __init__(self, state):
        """
        Initialize a new Memento instance.

        @param state: The state to save in this Memento.
        @type state: dict
        """
        self.__state = state

    @property
    def state(self):
        return self.__state


class Originator(object):
    """
    Originator base class as part of the Memento design pattern.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#memento-pattern}
    - External Mediator Pattern documentation: U{https://en.wikipedia.org/wiki/Memento_pattern}
    """

    def commit(self):
        """
        Commit this objects state to a memento.

        @return: A memento instance with this objects state.
        """
        return Memento(deepcopy(self.__dict__))

    def rollback(self, memento):
        """
        Rollback this objects state to a previous state.

        @param memento: The memento object holding the state to rollback to.
        @type memento: Memento
        """
        self.__dict__ = memento.state
