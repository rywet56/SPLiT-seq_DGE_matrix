# def mediator_func(func):
#     def adding_feature(a, b):
#         result = func(a, b)
#         return result + 1
#     return adding_feature
from functools import wraps


def mediator_func(func):
    def adding_feature(*args):
        result = func(*args) + 1
        return result

    return adding_feature


# @mediator_func
# def sum_it(a, b):
#     return a + b
# sum_it(7, 6)

class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        result = self.original_function(*args, **kwargs) + 30
        return result


def sum_it(a, b):
    return a + b


# sum_it_decorated = decorator_class(sum_it)
# sum_it_decorated(3, 4)
#
# sum_it(3,4)

from functools import wraps


def logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def log_wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return log_wrapper


def runtime(orig_func):
    import time

    @wraps(orig_func)
    def runtime_wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()
        print('{} ran in: {} sec'.format(orig_func.__name__, t2 - t1))
        return result

    return runtime_wrapper


def sum_it_all(a, b, c):
    return a + b + c


sum_it_all_decorated = runtime(logger(sum_it_all))
sum_it_all_decorated(2, 3, 4)

sum_it_all(2, 3, 4)

# sum_it_all_decorated = mediator_func(sum_it_all)
# sum_it_all_decorated(2, 3, 4)
