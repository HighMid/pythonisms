import pytest
from pythonics.TaskRunner import TaskRunner
import time

@pytest.fixture
def task_runner():
    return TaskRunner()

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