#######################################################
# How to serialize a dictionary with datetime objects #
#######################################################
import time


def print_execution_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print("{} || {} || lasted: {}s".format(__file__, func.__name__, time.time() - start))
        return res

    return inner


@print_execution_time
def name():
    time.sleep(0.1)
    print("Alice")


if __name__ == '__main__':
    name()
