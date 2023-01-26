import json
  
# custom class
class Student:
    def __init__(self, roll_no, name, batch):
        self.roll_no = roll_no
        self.name = name
        self.batch = batch
  
  
class Car:
    def __init__(self, brand, name, batch):
        self.brand = brand
        self.name = name
        self.batch = batch

class C(object):
    def __init__(self):
        self.x = 1
        self.y = 1


class D(object):
    __slots__ = ('x', 'y', 'car')
    def __init__(self):
        self.x = 1
        self.y = 1
        self.car =  Car('as', 'ff', 'cc')
    def __dict__1(self):
        return {s: getattr(self, s) for s in self.__slots__ if hasattr(self, s)}

class E(D):
    __slots__ = ()


class F(D):
    __slots__ = ('z',)
    def __init__(self):
        super(F, self).__init__()
        self.z = 1


def vars2(x):
    if hasattr(x, '__dict__'):
        return vars(x)
    else:
        ret = {slot: getattr(x, slot) for slot in x.__slots__}
        for cls in type(x).mro():
            spr = super(cls, x)
            if not hasattr(spr, '__slots__'):
                break
            for slot in spr.__slots__:
                ret[slot] = getattr(x, slot)
        return ret
import collections
try:
# Python 2.7 +
   basestring
except NameError:
   # Python 3.3 +
   basestring = str

def todict3(obj):        
    if isinstance(obj, dict):
        return dict((key.lstrip("_"), todict(val)) for key, val in obj.items())
    elif hasattr(obj, "_ast"):
        return todict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v) for v in obj]
    elif hasattr(obj, '__dict__'):
        return todict(vars(obj))
    elif hasattr(obj, '__slots__'):
        return todict(dict((name, getattr(obj, name)) for name in getattr(obj, '__slots__')))
    return obj
    
def todict2(obj):
        if isinstance(obj, basestring):
           return obj
        elif isinstance(obj, dict):
           return dict((key, todict(val)) for key, val in obj.items())
        elif isinstance(obj, collections.Iterable):
           return [todict(val) for val in obj]
        elif hasattr(obj, '__dict__'):
           return todict(vars(obj))
        elif hasattr(obj, '__slots__'):
           return todict(dict((name, getattr(obj, name)) for name in getattr(obj, '__slots__')))
        return obj

def todict(obj, classkey = None):
   if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
                data[k] = todict(v, classkey)
        return data
   elif hasattr(obj, "_ast"):
        return todict(obj._ast())
   elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
   elif hasattr(obj, "__dict__"):
        data = dict([(key, todict(value, classkey))
                for key, value in obj.__dict__.items()
                if not callable(value) and not key.startswith('_')
                ])
        if classkey is not None and hasattr(obj, "__class__"):
           data[classkey] = obj.__class__.__name__
        return data
   elif hasattr(obj, '__slots__'):
        return todict(dict((name, getattr(obj, name)) for name in getattr(obj, '__slots__')))
   else:
        return obj
   
def main():
    import pdb

    c = C()
    d = D()
    e = E()
    f = F()
    #pdb.set_trace()    
    #print(vars2(C()))
    #print(vars2(D()))
    #print(vars2(E()))
    #print(vars2(F()))
    print(c.__dict__)
    json_str = json.dumps(c.__dict__, indent=4)
    print(json_str)
    #print(d.__slots__)
    OUTPUT = '''\
{'y': 1, 'x': 1}
{'y': 1, 'x': 1}
{'y': 1, 'x': 1}
{'y': 1, 'x': 1, 'z': 1}
'''

if __name__ == '__main__':
    main()


  
# main function
if __name__ == "__main__1":
    
    # create two new student objects
    s1 = Student("85", "Swapnil", "IMT")
    s2 = Student("124", "Akash", "IMT")
  
    # create two new car objects
    c1 = Car("Honda", "city", "2005")
    c2 = Car("Honda", "Amaze", "2011")
  
    # convert to JSON format
    #jsonstr1 = json.dumps(s1.__dict__)
    #jsonstr2 = json.dumps(s2.__dict__)
    #jsonstr3 = json.dumps(c1.__dict__)
    #jsonstr4 = json.dumps(c2.__dict__)
    import pdb
    #pdb.set_trace()
    # print created JSON objects
    #print(jsonstr1)
    #print(jsonstr2)
    #print(jsonstr3)
    #print(jsonstr4)
    #print(todict(s1))
