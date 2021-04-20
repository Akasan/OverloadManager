from typing import Any
import sys
sys.path.append("../")
from OverloadManager.OverloadManager import OverloadManager

hoge = OverloadManager()

@hoge.register(int)
def _hoge(x):
    print(x, int)


@hoge.register(float)
def _hoge(x):
    print(x, float)

@hoge.register(Any)
def _hoge(*args, **kwargs):
    print(args)
    print(kwargs)


hoge(1)
# Output: 1 <class 'int'>
hoge(1.0)
# Output: 1.0 <class 'float'>
hoge(1, 1.0)
# Output: (1, 1.0)
#         {}

