from typing import Dict, Any


class InvalidArgumentsError(Exception):
    """ This raise when called execute with invalid arguments"""
    def __init__(self, mes):
        super(InvalidArgumentsError, self).__init__(mes)


class ArgumentOverwriteError(Exception):
    """ This raise when arguments already registered are to be registered again"""
    def __init__(self, mes):
        super(ArgumentOverwriteError, self).__init__(mes)


class OverloadManager:
    """ OverheadManager allows you to handle fucntions which have same name like Overhead in C/C++.
        You can register function like following
        
        1. the number of parameter is same, but the data type is not equal
        2. the number of parameter is not equal
        3. both 1 and 2 
    """
    def __init__(self, is_class: bool = False):
        self.IS_CLASS = is_class
        self.__param_func_pair: Dict[Any, Any] = {}

    def __call__(self, *args, **kwargs):
        """ new execution
        """
        # if self.IS_CLASS:
        #     _type = tuple([type(a) for a in kwargs.values()])
        # else:
        #     _type = tuple([type(a) for a in args] + [type(a) for a in kwargs.values()])
        _type = tuple([type(a) for a in args] + [type(a) for a in kwargs.values()])
        if self.IS_CLASS:
            _type = _type[1:]

        if not _type in self.__param_func_pair and not (Any,) in self.__param_func_pair:
            raise InvalidArgumentsError("You specify invalid arguments")
        
        elif not _type in self.__param_func_pair:
            self.__param_func_pair[(Any,)](*args, **kwargs)
        else:
            self.__param_func_pair[_type](*args, **kwargs)


    def register(self, *parameter) -> Any:
        """ register function
        Keyword Arguments:
            parameter -- parameter 
        """
        def _decorator(func):
            if parameter in self.__param_func_pair:
                print("You specify arguments already registered before.")
                flag = input("Will you register again(Yes: Y/y No: N/n)? (won't keep previous function) >>> ")
                if flag in ("N", "n"):
                    raise ArgumentOverwriteError("Arguments are already registered")

            self.__param_func_pair[parameter] = func

            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
        
            return wrapper

        return _decorator
    
    def describe_function(self):
        """ describe function you register"""
        for p, func in self.__param_func_pair.items():
            print(f"function name:{func}")
            print(f"parameter: {p}")
