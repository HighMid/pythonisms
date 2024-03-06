## Pythonics

### Iterators/Generators on a Custom Collection

>We'll create a custom collection class that implements the iterator protocol, allowing it to be used in a for loop, list comprehension, and be convertible to a list.

```
class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            number = self.current
            self.current += 1
            return number
        raise StopIteration

# Use in a for loop
for num in CustomRange(1, 4):
    print(num)  # Prints 1, 2, 3

# List comprehension
squares = [x*x for x in CustomRange(1, 4)]
print(squares)  # Prints [1, 4, 9]

# Convert to list
numbers_list = list(CustomRange(1, 4))
print(numbers_list)  # Prints [1, 2, 3]
```

### Decorator Examples

1. Timing a Function

```
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to complete.")
        return result
    return wrapper

@timeit
def slow_function():
    time.sleep(2)

slow_function()
```

2. Slowing Down a Function

```
def slow_down(func):
    def wrapper(*args, **kwargs):
        time.sleep(1)  # Sleep for 1 second
        return func(*args, **kwargs)
    return wrapper

@slow_down
def fast_function():
    print("That was too fast!")

fast_function()
```

### Using Dunder Methods

1. Equality for Custom Data Structures

```
class Box:
    def __init__(self, items):
        self.items = items

    def __eq__(self, other):
        return self.items == other.items

box1 = Box([1, 2, 3])
box2 = Box([1, 2, 3])
print(box1 == box2)  # True
```

2. Truthy/Falsy Custom Data Structure

```
class Container:
    def __init__(self, content):
        self.content = content

    def __bool__(self):
        return bool(self.content)

empty_container = Container([])
full_container = Container([1, 2, 3])

print(bool(empty_container))  # False
print(bool(full_container))   # True
```

### Tests

1. `pip install -r requirements.txt`
2. `pytest tests/test_taskrunner.py`, if in root directory
    - `pytest test_taskrunner.py` if inside test directory

### Tested

```
def test_timeit_decorator_on_fast_task(task_runner, capsys):
    task_runner.fast_task()
    captured = capsys.readouterr()
    assert "Fast task is executed." in captured.out
    assert "Method fast_task took" in captured.out

def test_slow_down_decorator_on_slow_task(task_runner):
    start_time = time.time()
    task_runner.slow_task()
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert elapsed_time >= 1, "The slow_task method did not take at least 1 second to execute, indicating the slow_down decorator may not be working as expected."
```