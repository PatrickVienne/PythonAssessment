########################################################################
# Make a decorator which prints the decorated functions execution time #
########################################################################
import time


@print_execution_time
def name():
    time.sleep(0.1)
    print("Alice")


if __name__ == '__main__':
    name()
