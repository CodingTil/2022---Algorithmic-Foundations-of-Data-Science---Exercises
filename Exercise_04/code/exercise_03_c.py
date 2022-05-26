import functools
import math


def length(v):
    return math.sqrt(functools.reduce(lambda a, b: a + b, map(lambda v_i: v_i ** 2, v)))


def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


def matrix_times_vector(A, v):
    Av = list()
    for i in range(len(A)):
        assert(len(A[i]) == len(v))
        Av.append(functools.reduce(
            lambda a, b: a + b, map(lambda item: A[i][item[0]] * item[1], enumerate(v))))
    return Av


def power_iteration(A, x):
    x_length = length(x)
    v = tuple(map(lambda x_i: x_i / x_length, x))
    old_trunc_v = tuple(map(lambda v_i: truncate(v_i, 3), v))
    while True:

        Av = matrix_times_vector(A, v)
        Av_length = length(Av)
        v = tuple(map(lambda v_i: v_i / Av_length, Av))

        # check if does not converge no more
        new_trunc_v = tuple(map(lambda v_i: truncate(v_i, 3), v))
        if(old_trunc_v == new_trunc_v):
            break
        old_trunc_v = new_trunc_v
    return v


if __name__ == '__main__':
    C = [
        [18, 18],
        [18, 70]
    ]
    v = (1,1)
    v_power = power_iteration(C,v)
    print(tuple(map(lambda v_i: round(v_i, 3), v_power)))
