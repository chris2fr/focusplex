class TaskLevelCounter:
    counter = 1

tlc = TaskLevelCounter()

print(tlc.counter)

TaskLevelCounter.counter += 1

print(tlc.counter)
print(TaskLevelCounter.counter)