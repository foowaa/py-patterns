"""
命令模式

在软件开发中，我们经常需要向某些对象发送请求（调用其中的某个或某些方法），但是并不知道请求的接收者是谁，也不知道被请求的操作是哪个，此时，我们特别希望能够以一种松耦合的方式来设计软件，使得请求发送者与请求接收者能够消除彼此之间的耦合，让对象之间的调用关系更加灵活，可以灵活地指定请求接收者以及被请求的操作。命令模式为此类问题提供了一个较为完美的解决方案。
命令模式可以将请求发送者和接收者完全解耦，发送者与接收者之间没有直接引用关系，发送请求的对象只需要知道如何发送请求，而不必知道如何完成请求。
命令模式定义如下：
命令模式(Command Pattern)：将一个请求封装为一个对象，从而让我们可用不同的请求对客户进行参数化；对请求排队或者记录请求日志，以及支持可撤销的操作。命令模式是一种对象行为型模式，其别名为动作(Action)模式或事务(Transaction)模式。

"""
from abc import ABCMeta, abstractmethod

'''
receiver, command, invoker
see: https://github.com/tylerlaberge/PyPattyrn#command-pattern
'''


class Receiver(object, metaclass=ABCMeta):

    def action(self, name, *args, **kwargs):
        """
        Delegates which method to be called for a desired action.

        @param name: The name of the action to execute.
        @type name: str
        @param args: Any arguments for the action.
        @param kwargs: Any keyword arguments for the action.
        """
        try:
            return getattr(self, name)(*args, **kwargs)
        except AttributeError:
            raise AttributeError('Invalid Action.')


class Command(object, metaclass=ABCMeta):

    def __init__(self, receiver):
        """
        Initialize a new command instance.

        @param receiver: The receiver for this command to use.
        @type receiver: Receiver
        """
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        """
        Abstract method for executing an action.
        """
        pass

    @abstractmethod
    def unexecute(self):
        """
        Abstract method for unexecuting an action.
        """
        pass


class Invoker(object, metaclass=ABCMeta):

    def __init__(self, valid_commands):
        """
        Initialize a new Invoker instance.

        @param valid_commands: A list of command classes this invoker can handle.
        """
        self._history = []
        self._valid_commands = valid_commands

    def execute(self, command):
        """
        Execute a command.

        @param command: A command for the invoker to execute.
        @type command: Command
        """
        if command.__class__ not in self._valid_commands:
            raise AttributeError('Invalid Command')
        else:
            self._history.append(command)
            return command.execute()

    def undo(self):
        """
        Undo the last command.
        """
        return self._history.pop().unexecute()
