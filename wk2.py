from time import perf_counter
import random

# User input: Two numbers in a single line (small and large list sizes)
n, m = map(int, input().split())

# Number of trials for averaging
TRIALS = 100

# Dictionary sizes
small_dict = {i: i for i in range(n)}
large_dict = {i: i for i in range(m)}

# Function to measure execution time using perf_counter
def measure_time(func):
    times = []
    for _ in range(TRIALS):
        t1_start = perf_counter()  # Start time
        func()
        t1_end = perf_counter()  # End time
        times.append(t1_end - t1_start)  # Store elapsed time
    return sum(times) / len(times)  # Return mean time

# Define each operation as a function

def add_to_beginning_small():
    l = list(range(n))
    l.insert(0, -1)

def add_to_beginning_large():
    l = list(range(m))
    l.insert(0, -1)

def add_to_end_small():
    l = list(range(n))
    l.append(-1)

def add_to_end_large():
    l = list(range(m))
    l.append(-1)

def remove_from_beginning_small():
    l = list(range(n))
    l.pop(0)

def remove_from_beginning_large():
    l = list(range(m))
    l.pop(0)

def remove_from_end_small():
    l = list(range(n))
    l.pop()

def remove_from_end_large():
    l = list(range(m))
    l.pop()

def check_presence_in_small():
    l = list(range(n))
    return -1 in l

def check_presence_in_large():
    l = list(range(m))
    return random.choice(l) in l

def check_presence_not_in_small():
    l = list(range(n))
    return 99999 in l

def check_presence_not_in_large():
    l = list(range(m))
    return -1 in l

def check_key_in_small():
    return random.choice(list(small_dict.keys())) in small_dict

def check_key_in_large():
    return random.choice(list(large_dict.keys())) in large_dict

def check_key_not_in_small():
    return -1 in small_dict

def check_key_not_in_large():
    return -1 in large_dict

# List of tests
results = [
    measure_time(add_to_beginning_small),
    measure_time(add_to_beginning_large),
    measure_time(add_to_end_small),
    measure_time(add_to_end_large),
    measure_time(remove_from_beginning_small),
    measure_time(remove_from_beginning_large),
    measure_time(remove_from_end_small),
    measure_time(remove_from_end_large),
    measure_time(check_presence_in_small),
    measure_time(check_presence_in_large),
    measure_time(check_presence_not_in_small),
    measure_time(check_presence_not_in_large),
    measure_time(check_key_in_small),
    measure_time(check_key_in_large),
    measure_time(check_key_not_in_small),
    measure_time(check_key_not_in_large),
]

# Print results (one per line, as required)
for result in results:
    print(result)
