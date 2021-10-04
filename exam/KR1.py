import typing
import collections
import types


class Logger(type):

    @staticmethod
    def call_counter(func, instance):
        LogItem = collections.namedtuple('LogItem', ['name', 'args', 'kwargs', 'result'])
        print(instance.LogItem(1, 1, 1, 1))

        def wrapper(*args, **kwargs):
            print('wrapper')
            result = func(*args, **kwargs)
            # print(self.LogItem(1, 1, 1, 1))
            instance.log.append(LogItem(func.__name__, args[1:], kwargs, result))
            instance.last_log = instance.log[-3:] if len(instance.log) >= 3 else instance.log
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
