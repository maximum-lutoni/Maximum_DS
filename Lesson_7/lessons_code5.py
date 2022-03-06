from datetime import datetime

def timeit(func):
    def wrapper(val):
        start = datetime.now()
        res = func(val)
        end = datetime.now()
        print(f"time: {end - start}")
        return res
    return wrapper
@timeit
def get_list_1(val):
    return [x for x in range(val) if x % 2]
@timeit
def get_list_2(val):
    new_list =[]
    for x in range(val):
        if x%2:
            new_list.append(x)
    return new_list

val = 10000000
a = get_list_1(val)
b = get_list_2(val)
