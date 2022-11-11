import time
from datetime import datetime


def time_slow( **kwargs):
    def wrapper(func):
        start_time = time.time()
        if kwargs.get('threshold') is None:
            print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
            print(f'Execution time:  %s seconds' % (time.time() - start_time))
        else:
            if kwargs['threshold'] < (time.time() - start_time):
                print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
                print(f'Execution time:  %s seconds' % (time.time() - start_time))

    return wrapper


@time_slow(threshold=0.1)
def my_fast():
    print('function ended')
