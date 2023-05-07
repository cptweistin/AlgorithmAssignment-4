# -*- coding: utf-8 -*-
"""
Justin  魏才金
"""

import time

# Pure Recursive Method
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Dynamic Programming Method
def fibonacci_dynamic(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# Measure execution time for n=10,20,...,100
n_values = list(range(10, 101, 10))
recursive_times = []
dynamic_times = []

for n in n_values:
    start_time = time.time()
    fibonacci_recursive(n)
    recursive_times.append(time.time() - start_time)

    start_time = time.time()
    fibonacci_dynamic(n)
    dynamic_times.append(time.time() - start_time)
    
# Compute F(n+1) using dynamic programming
n = 1000 # Replace with the maximum n value that didn't crash your computer
fibonacci_dynamic(n+1) # Compute F(n+1) without crashing your computer


# Plot results as line chart
import matplotlib.pyplot as plt
plt.plot(n_values, recursive_times, label='Pure Recursive')
plt.plot(n_values, dynamic_times, label='Dynamic Programming')
plt.xlabel('n')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.show()


