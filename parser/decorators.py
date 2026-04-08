import time
from functools import wraps

def timer(func):

  @wraps(func)  #saves function's original metadata to the wrapper
  def wrapper(*args, **kwargs):
    start_time: float = time.perf_counter()
    result = func(*args, **kwargs)
    end_time: float = time.perf_counter()

    runtime: float = end_time - start_time

    print(f"Ran {func.__name__} in {runtime:.2f} seconds")

    return result
  return wrapper