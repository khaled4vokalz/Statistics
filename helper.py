from random import randint

def get_random_friends_array():
    for _ in range(100):
        yield randint(0,101)

# for now we generate random numbers between 0 and 100 as friends counter
num_friends = list(get_random_friends_array())

def dot(v, w):
        """v_1 * w_1 + ... + v_n * w_n"""
        return sum([v_i * w_i for v_i, w_i in zip(v, w)])


def sum_of_squares(v):
        return dot(v, v)