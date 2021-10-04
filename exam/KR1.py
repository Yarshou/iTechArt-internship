import typing
import collections
import types


class Logger(type):


    def __new__(mcs, name, bases, attrs):
        Point = collections.namedtuple('LogItem', ['name', 'args', 'kwargs', 'result'])
        attrs['LogItem'] = Point(str(), list(), dict(), typing.Any)
        new_attrs = dict()
        new_attrs['log'] = list()
        for elem in attrs.keys():
            new_attrs[elem] = attrs[elem]
            if isinstance(attrs[elem], types.FunctionType) and not elem.startswith('_'):
                pass
                # new_attrs['log'].append(Point(name=elem, args=))
        return super(Logger, mcs).__new__(mcs, name, bases, new_attrs)
