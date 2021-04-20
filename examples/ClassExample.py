from typing import Any
from OverloadManager import OverloadManager


class Hoge:
    _init = OverloadManager(is_class=True)

    @_init.register(int)
    def __init__(self, x):
        self.x = x
        self.type = int

    @_init.register(float)
    def __init__(self, x):
        self.x = x
        self.type = float

    @_init.register(Any)
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.type = Any

    def __init__(self, *args, **kwargs):
        self._init(self, *args, **kwargs)


hoge = Hoge(1)
print(hoge.x, hoge.type)
# Output: 1 <class 'int'>

hoge = Hoge(1.0)
print(hoge.x, hoge.type)
# Output: 1.0 <class 'float'>

hoge = Hoge(1, 1.0)
print(hoge.args, hoge.kwargs, hoge.type)
# Output: (1, 1.0) {} typing.Any
