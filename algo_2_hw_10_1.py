import random
import time
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Використання середнього елемента як опорного
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())  # Копія масиву, щоб уникнути зміни оригіналу
    return time.time() - start_time

sizes = [10000, 50000, 100000, 500000]
times_randomized = []
times_deterministic = []

for size in sizes:
    arr = [random.randint(0, 1000000) for _ in range(size)]
    
    time_randomized = sum(measure_time(randomized_quick_sort, arr) for _ in range(5)) / 5
    time_deterministic = sum(measure_time(deterministic_quick_sort, arr) for _ in range(5)) / 5
    
    times_randomized.append(time_randomized)
    times_deterministic.append(time_deterministic)
    
    print(f"Розмір масиву: {size}")
    print(f"Рандомізований QuickSort: {time_randomized:.4f} секунд")
    print(f"Детермінований QuickSort: {time_deterministic:.4f} секунд")
    print()

# Побудова графіка
plt.figure(figsize=(8,6))
plt.plot(sizes, times_randomized, label="Рандомізований QuickSort", marker="o")
plt.plot(sizes, times_deterministic, label="Детермінований QuickSort", marker="x")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.legend()
plt.grid()
plt.show()
