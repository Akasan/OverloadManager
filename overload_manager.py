from pprint import pprint


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
            self.__func[self.__func_num] = func
            self.__func_num += 1
            self.__param_func_pair[parameter] = func

            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
        
            return wrapper
        return _decorator
    
    def describe_function(self):
        for p, func in self.__param_func_pair.items():
            print(f"function name:{func}")
            print(f"parameter: {p}")

    def execute(self, *args, **kwargs):
        type_list = tuple([type(i) for i in kwargs.values()])
        func = self.__param_func_pair[type_list]
        func(**kwargs)


overload = OverloadManager()
