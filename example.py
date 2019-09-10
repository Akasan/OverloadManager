# from overhead_manager import OverheadManager
from overhead_manager import overhead
import math


@overhead.register(int, float)
def hoge(a, b):
    print(a * math.cos(b))


@overhead.register(float, float)
def hoge(a, b):
    print(a * math.sin(b))


@overhead.register(int, float, str)
def hoge(a, b, c):
    print(a)
    print(b)
    print(c)


overhead.execute(a=10, b=2.0)
overhead.execute(a=10.0, b=2.0)
