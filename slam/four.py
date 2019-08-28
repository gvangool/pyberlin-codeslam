import timeit

from slam.two import create_array, sorted_array_bisect, sorted_array

if __name__ == "__main__":
    for length in (8, 32, 128):
        array = list(create_array(length))
        t1 = timeit.timeit(lambda: sorted_array_bisect(array), number=1000)
        t2 = timeit.timeit(lambda: sorted_array(array), number=1000)
        print(f"{len(array)=}")
        print(f"sorted_array_bisect: {t1}")
        print(f"sorted_array       : {t2}")
