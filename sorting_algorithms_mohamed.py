import random
import time


# 1. Quick Sort
def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)


# 2. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# 3. Heap Sort
def heapify(arr, size, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, size, largest)


def heap_sort(arr):
    size = len(arr)

    # Build a max-heap.
    for root in range(size // 2 - 1, -1, -1):
        heapify(arr, size, root)

    # Move each maximum to the end of the active heap.
    for end in range(size - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)


# Compare the three algorithms on identical input values.
if __name__ == "__main__":
    sizes = [100, 1000, 10000, 100000, 1000000]

    print("Elements | Quick Sort | Merge Sort | Heap Sort (seconds)")

    for size in sizes:
        # Random values without duplicates.
        original = random.sample(range(1, 10000001), size)

        quick_array = original.copy()
        start_time = time.perf_counter()
        quick_sort(quick_array, 0, len(quick_array) - 1)
        quick_time = time.perf_counter() - start_time

        merge_array = original.copy()
        start_time = time.perf_counter()
        merge_sort(merge_array)
        merge_time = time.perf_counter() - start_time

        heap_array = original.copy()
        start_time = time.perf_counter()
        heap_sort(heap_array)
        heap_time = time.perf_counter() - start_time

        # Check correctness outside the timed sections.
        expected = sorted(original)
        assert quick_array == expected
        assert merge_array == expected
        assert heap_array == expected

        print(f"{size:>8,} | {quick_time:.6f} | "
              f"{merge_time:.6f} | {heap_time:.6f}")
