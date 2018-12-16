"""
中介者模式
可以使对象之间的关系数量急剧减少，通过引入中介者对象，可以将系统的网状结构变成以中介者为中心的星形结构，如图20-5所示。在这个星形结构中，同事对象不再直接与另一个对象联系，它通过中介者对象与另一个对象发生相互作用。中介者对象的存在保证了对象结构上的稳定，也就是说，系统的结构不会因为新对象的引入带来大量的修改工作。
"""

# see: https://github.com/tylerlaberge/PyPattyrn#mediator-pattern

from collections import defaultdict

class Mediator(object):

    def __init__(self):
        """
        Initialize a new Mediator instance.
        """
        self.signals = defaultdict(list)

    def signal(self, signal_name, *args, **kwargs):
        """
        Send a signal out to all connected handlers.
        @param signal_name: The name of the signal.
        @type signal_name: Str
        @param args: Positional arguments to send with the signal.
        @param kwargs: Keyword arguments to send with the signal.
        """
        for handler in self.signals[signal_name]:
            handler(*args, **kwargs)

    def connect(self, signal_name, receiver):
        """
        Connect a receiver to a signal.
        @param signal_name: The name of the signal to connect the receiver to.
        @type signal_name: str
        @param receiver: A handler to call when the signal is sent out.
        """
        self.signals[signal_name].append(receiver)

    def disconnect(self, signal_name, receiver):
        """
        Disconnect a receiver from a signal.
        @param signal_name: The name of the signal to disconnect the receiver from.
        @type signal_name: str
        @param receiver: The receiver to disconnect from the signal.
        """
        try:
            self.signals[signal_name].remove(receiver)
        except ValueError:
            pass
