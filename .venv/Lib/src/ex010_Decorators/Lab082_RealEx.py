import time

def print_logs(func):

    def wrapper():
        print("Start of the logs")
        func()
        print("End of the logs")
        return wrapper
def time_decorator(func):
    def wrapper():
        start_time=time.time()
        print(start_time)
        func()

        @time_decorator
        @print_logs
        def