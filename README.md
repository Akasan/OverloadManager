# OverloadManager

## Description
This repo provides you to use overload in Python.
You can easily use functions which have the same name like C/C++.

## HOW TO
First, please import decorator as below
```python
from overload_manager import OverloadManager

# I recommend the instance name like <function_name>_manager
# For this example, like below
hoge_manager = OverloadManager()
```

Next, add decorator to functions you want to handle as overload function like below.
```python
@hoge_manager.register(int)
def hoge(a):
    print("This function can only print integer")
    print(f"value: {a}, type: {type(a)}")

@hoge_manager.register(float)
def hoge(a):
    print("This function can only print float")
    print(f"value: {a}, type: {type(a)}")

@hoge_manager.register(int, float)
def hoge(a, b):
    print("This function can only print int and float at once")
    print(f"value: {a}, type: {type(a)}")
    print(f"value: {b}, type: {type(b}}")
```
You can register function by calling `overload.register`.
When you call it, you have to set arguments' data-type. If you set same argument more than twice, they are regarded as same function.

Finally, you can execute function as below.
```python
hoge_manager(a=10)
# result:
# This function can only print integer
# value: 10, type: <class `int`>

hoge_manager(a=10.0)
# result:
# This function can only print float
# value: 10.0, type: <class `float`>

hoge_manager(a=10, b=10.0)
# result:
# This function can only print int and float at once
# value: 10, type: <class `int`>
# value: 10.0, type: <class `float`>
```

So far, you have to call function with parameter name and value both.
You can call function like below
```python
# OK
hoge_manager(a=10.0)

# NG
hoge_manager(10.0)
```

## Scheduled for implementation
- support for class method
