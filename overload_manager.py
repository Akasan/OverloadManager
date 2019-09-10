from pprint import pprint


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
    def __init__(self):
        self.__func = {}
        self.__func_num = 1
        self.__param_func_pair = {}

    def register(self, *parameter):
        """ register function

        Keyword Arguments:
            parameter -- parameter 
        """
        def _decorator(func):
            if parameter in self.__param_func_pair:
                raise ArgumentOverwriteError("Arguments are already registered")

            self.__func[self.__func_num] = func
            self.__func_num += 1
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

    def execute(self, *args, **kwargs):
        """ execute function according to arguments you set this function
            This function automatically check arguments and switch functions

        Arguments:
            args -- arguments without keyword

        Keyword Arguments:
            kwargs -- arguments with keyword
        """
        type_pair = tuple([type(i) for i in kwargs.values()])
       
        if not type_pair in self.__param_func_pair:
            raise InvalidArgumentsError("You specify invalid arguments")

        func = self.__param_func_pair[type_pair]
        func(**kwargs)


overload = OverloadManager()
