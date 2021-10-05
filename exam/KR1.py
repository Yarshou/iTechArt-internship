import typing
import collections
import types


class Logger(type):

    def call_counter(self, func, instance):
        LogItem = self.LogItem

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            instance.log.append(LogItem(func.__name__, args[1:], kwargs, result))
            instance.last_log = instance.log[2::-1] if len(instance.log) >= 5 else instance.log[::-1]
            return result

        return wrapper

    def __call__(cls, *args, **kwargs):
        instance = super(Logger, cls).__call__(*args, **kwargs)
        for attr in cls.__dict__:
            if callable(cls.__dict__[attr]) and not attr.startswith("_"):
                setattr(cls, attr, cls.call_counter(cls.__dict__[attr], instance))
        setattr(instance, 'log', list())
        setattr(instance, 'last_log', list())
        return instance

    def __new__(mcs, name, bases, attrs):
        attrs['LogItem'] = collections.namedtuple('LogItem', ['name', 'args', 'kwargs', 'result'])
        return super(Logger, mcs).__new__(mcs, name, bases, attrs)
