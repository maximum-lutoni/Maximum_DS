def singleton(_class):
    def redefine_new(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(_class,cls).__new__(cls)
        return cls.instance
    _class.__new__=redefine_new
    return _class

@singleton
class One:
    pass

class Two:
    pass

a=One()
b=One()
print(id(a), id(b), id(a) == id(b))

b=Two()
c=Two()
print(id(b), id(c), id(b) == id(c))