import time

def crono(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        result = end - start
        return result
    return wrapper