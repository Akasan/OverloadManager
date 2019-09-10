# from overhead_manager import OverheadManager
from overload_manager import overload


@overload.register(int)
def hoge(a):
    print("This function can only print integer")
    print(f"value: {a}, type: {type(a)}")

@overload.register(float)
def hoge(a):
    print("This function can only print float")
    print(f"value: {a}, type: {type(a)}")


overload.execute(a=10)
# result:
# This function can only print integer
#value: 10, type: <class `int`>

overload.execute(a=10.0)
# result:
# This function can only print float
# value: 10.0, type: <class `float`>

