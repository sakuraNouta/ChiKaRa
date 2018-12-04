import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)
    return wrapper

@my_decorator
def func():
    time.sleep(0.8)

func()
