from datetime import datetime
import time


def time_slow(func):
    def wrapper():
        start_time = time.time()
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'Execution time:  %s seconds' % (time.time() - start_time))
        print(f'{"*" * 30}')
        func()
    return wrapper


@time_slow
def daily_backup():
    print('Daily backup job has finished.')


daily_backup()
