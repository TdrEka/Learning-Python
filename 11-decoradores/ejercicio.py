# Agregar a una clase Foo un metodo
# llamado method_instance and another one called method_class
# of class and instance
# In a dynamic way, and then make a decorator that will decorate that class automatically adding the same functionality


def add_methods(cls):
    setattr(cls, 'method_instance', lambda self: "instance method")
    setattr(cls, 'method_class', classmethod(lambda cls: "class method"))
    return cls

class Foo:
    def __init__(self):
        self.value = "I'm a Foo D: "


def instance_method(self):
    return f"Instance method called on {self.value}"

def class_method(cls):
    return f"Class method called on {cls.__name__}"

setattr(Foo, 'method_instance', instance_method)
setattr(Foo, 'method_class', classmethod(class_method))

@add_methods
class Potato:
    pass

