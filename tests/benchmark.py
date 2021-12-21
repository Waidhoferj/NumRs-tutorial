from timeit import timeit
from numrs import Array


def benchmark():
    list1 = [num for num in range(1_000_000)]
    list2 = [num for num in range(1_000_000)]
    arr1 = Array(list1)
    arr2 = Array(list2)

    add_arrays = lambda: arr1 + arr2
    add_lists = lambda: [x + y for x, y in zip(list1, list2)]

    times = {
        # "list": timeit(add_lists, number=1000),
        "array": timeit(add_arrays, number=1000),
    }

    print(times)
    # print(f"Rust is {times['list']/ times['array']} times faster")


if __name__ == "__main__":
    benchmark()
