import time
import functools

class TaskRunner:

    @staticmethod
    def timeit(method):
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = method(*args, **kwargs)
            end_time = time.time()
            print(f"Method {method.__name__} took {end_time - start_time} seconds to complete.")
            return result
        return wrapper

    @staticmethod
    def slow_down(method):
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            time.sleep(1)  # Sleep for 1 second
            return method(*args, **kwargs)
        return wrapper

    @timeit.__func__
    def fast_task(self):
        """A fast task that completes instantly for demonstration."""
        print("Fast task is executed.")

    @slow_down.__func__
    def slow_task(self):
        """A slow task that requires deliberate slowing down."""
        print("Slow task is executed.")
