import types


def pep8_warrior(class_name, bases, attrs) -> type:
    new_attrs = dict()
    for elem in attrs.keys():
        if elem.startswith('__'):
            new_attrs[elem] = attrs[elem]
        else:
            if isinstance(attrs[elem], types.FunctionType):
                new_attrs[elem.lower()] = attrs[elem]
            if isinstance(attrs[elem], type):
                cls_name = "".join(list(map(lambda x: x.title(), attrs[elem].__name__.replace(" ", "").split('_'))))
                new_attrs[cls_name] = attrs[elem]
            if isinstance(attrs[elem], (str, int, float, dict, list, tuple)):
                new_attrs[elem.upper()] = attrs[elem]
    return type(class_name, bases, new_attrs)


class Pep8Warrior(type):

    def __new__(mcs, name, bases, attrs):
        new_attrs = dict()
        for elem in attrs.keys():
            if elem.startswith('__'):
                new_attrs[elem] = attrs[elem]
            else:
                if isinstance(attrs[elem], types.FunctionType):
                    new_attrs[elem.lower()] = attrs[elem]
                if isinstance(attrs[elem], type):
                    cls_name = "".join(list(map(lambda x: x.title(), attrs[elem].__name__.replace(" ", "").split('_'))))
                    new_attrs[cls_name] = attrs[elem]
                if isinstance(attrs[elem], (str, int, float, dict, list, tuple)):
                    new_attrs[elem.upper()] = attrs[elem]

        return super(Pep8Warrior, mcs).__new__(mcs, name, bases, new_attrs)
