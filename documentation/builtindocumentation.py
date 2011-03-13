# This file denotes the built-in python API. It is imported into every file which is parsed.
class Exception:
	pass

class __kdevpythondocumentation_builtin_list():
    def append(obj): pass
    def extend(obj): return []

class __kdevpythondocumentation_builtin_dict():
    def append(obj): pass

class __kdevpythondocumentation_builtin_string():
    def replace(before, after): return ""
    
class __kdevpythondocumentation_builtin_float():
    pass


def abs(x): return 0
def all(iterable): return True
def any(iterable): return True
def bin(x): return ""
def bool(x = False): return True
def bytearray(source = None, encoding = None, errors = None): return []
def callable(object): return True
def chr(i): return ""
def classmethod(function): return None
def cmp(x, y): return 0
def compile(source, filename, mode, flags = None, dont_inherit = None): return None
def complex(real = 0, imag = 0): return 1+3j
def delattr(obj, name): return None
def dict(arg = None): return {"string" : None}
def dir(obj = None): return {"string" : None}
def divmod(a, b): return 0
def enumerate(sequence, start = 0): return [(0, 0)]
def eval(expression, glob = None, loc = None): return None
def execfile(filename, glob = None, loc = None): return None
def file(filename, mode = None, bufsize = None): return None
def filter(function, iterable): return []
def float(x = 0): return 0.0
def format(value, format_spec = None): return ""
def frozenset(iterable = None): return ()
def getattr(obj, name, default = None): return None
def globals(): return {}
def hasattr(obj, name): return bool
def hash(obj): return 0
def hex(x): return 0x0
def id(obj): return 0
def input(prompt = None): return None
def isinstance(obj, cls): return True
def issubclass(cls, info): return True
def iter(o, s = None): return __kdevpythondocumentation_builtin_iterator()
def len(s): return 0
def list(i = None): return []
def locals(): return {}
def long(x = None, base = None): return 0L
def map(func, iterab): return []
def max(lst, args = None, key = None): return 0
def memoryview(obj): return None
def min(lst, default = None): return 0
def next(iterator, default = None): return iterator[0]
def object(): return None
def oct(x): return 0o0
def open(filename, mode = None, bufsize = None): return __kdevpythondocumentation_builtin_fileObject()
def ord(c): return 0
def pow(x, y, z = 0): return 0.0
def property(fget = 0, fset = 0, fdel = 0, doc = 0): return 0
def range(start = 0, stop = 0, step = 0): return []
def raw_input(prompt = ""): return ""
def reduce(function, iterable, init = None): return None
def reload(module) : return None
def repr(object): return ""
def reversed(seq): return __kdevpythondocumentation_builtin_iterator()
def round(x, n=0): return 0.0
def set(iterable = None): return ( )
def setattr(obj, name, value): return None
def slice(start = 0, stop = 0, step = 0): return __kdevpythondocumentation_builtin_sliceObject()
def sorted(iterable, cmpre = None, key = None, reverse = False): return []
def staticmethod(function): return function
def str(obj = None): return ""
def sum(iterable): return 0.0
def super(_type, obj = None): return None
def tuple(iterable = None): return ()
def type(object): return  __kdevpythondocumentation_builtin_typeObject()
def unichr(i): return ""
def unicode(obj = None, encoding = None, errors = None): return ""
def vars(obj): return None
def xrange(start = 0, stop = 0, step = 0): return []
def zip(iterable = None): return []
def __import__(name, globa = None, loca = None, fromlist = None, level = 0): return None
