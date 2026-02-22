import threading
import time


def sleeper_sort(num, sorted_list, lock, sleep_factor):
    time.sleep(num / sleep_factor)  # sleep for num/1000 seconds
    with lock:
        sorted_list.append(num)


def sleep_sort(numbers, sleep_factor=100):
    sorted_list = []
    lock = threading.Lock()
    threads = []

    for num in numbers:
        thread = threading.Thread(
            target=sleeper_sort, args=(num, sorted_list, lock, sleep_factor)
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return sorted_list


if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Sorted numbers:", sleep_sort(nums))
