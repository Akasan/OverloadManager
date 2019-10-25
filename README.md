# OverloadManager

## Description
This repo provides you to use overload in Python.
You can easily use functions which have the same name like C/C++.

## HOW TO
First, please import decorator as below
```python
from overload_manager import overload
```

Next, add decorator to functions you want to handle as overload function like below.
```python
@overload.register(int)
def hoge(a):
    print("This function can only print integer")
    print(f"value: {a}, type: {type(a)}")

@overload.register(float)
def hoge(a):
    print("This function can only print float")
    print(f"value: {a}, type: {type(a)}")

@overload.register(int, float)
def hoge(a, b):
    print("This function can only print int and float at once")
    print(f"value: {a}, type: {type(a)}")
    print(f"value: {b}, type: {type(b}}")
```
You can register function by calling overload.register.
When you call it, you have to set arguments' data-type. If you set same argument more than twice, they are regarded as same function.

Finally, you can execute function as below.
```python
overload.execute(a=10)
# result:
# This function can only print integer
# value: 10, type: <class `int`>

overload.execute(a=10.0)
# result:
# This function can only print float
# value: 10.0, type: <class `float`>

overload.execute(a=10, b=10.0)
# result:
# This function can only print int and float at once
# value: 10, type: <class `int`>
# value: 10.0, type: <class `float`>
```

## Scheduled for implementation
- support for class method
