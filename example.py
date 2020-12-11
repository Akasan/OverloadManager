# from overhead_manager import OverheadManager
from OverloadManager.OverloadManager import OverloadManager


hoge_manager = OverloadManager()

@hoge_manager.register(int)
def hoge(a):
    print("This function can only print integer")
    print(f"value: {a}, type: {type(a)}")

@hoge_manager.register(float)
def hoge(a):
    print("This function can only print float")
    print(f"value: {a}, type: {type(a)}")

@hoge_manager.register(str)
def hoge(a):
    print("This function can only print float")
    print(f"value: {a}, type: {type(a)}")


hoge_manager(a=10)
# result:
# This function can only print integer
#value: 10, type: <class `int`>

hoge_manager(a=10.0)
# result:
# This function can only print float
# value: 10.0, type: <class `float`>

hoge_manager(a="10.0")
