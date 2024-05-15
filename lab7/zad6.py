import logging
import functools
import time


def log(level):
    def decorator(obj):
        if isinstance(obj, type):
            return log_class(obj, level)
        else:
            return log_function(obj, level)

    return decorator


def log_function(func, level):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time

        logger = logging.getLogger(func.__module__)
        logger.log(level, f"Function {func.__name__} called with args={args}, kwargs={kwargs}, returned {result}, duration: {duration:.3f} seconds")

        return result

    return wrapper


def log_class(cls, level):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self._instance = cls(*args, **kwargs)
            self.logger = logging.getLogger(cls.__module__)
            self.logger.log(level, f"Class {cls.__name__} created with args={args}, kwargs={kwargs} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")

            self.__class__ = type(self._instance.__class__.__name__,
                                  (self.__class__, self._instance.__class__),
                                  {})  #zmienia na klase dziedziczaca po klasie ktora chcemy zastapic
            self.__dict__ = self._instance.__dict__ #slownik atrybutow

    return Wrapper


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)


    @log(level=logging.INFO)
    def func(x, y):
        for i in range(1000000):
            x += y
        return x


    @log(level=logging.ERROR)
    class TestClass:
        def __init__(self, x, y, **kwargs):
            self.x = x - 1
            self.y = y + 1
            self.kwargs = kwargs


    result = func(3, y = 5)
    print("Result of func function in result:", result)

    print()

    testClass = TestClass(0, y=10, abc = -1)
    print("x and y in testClass", testClass.x, testClass.y)

    