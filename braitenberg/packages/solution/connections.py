from typing import Tuple
import math
import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")

    full = shape[0]

    res[full:, :(shape[1] // 2)] = 1
    res[full:, ((shape[1] // 2) + 1):] = -1

    for i in range(200, full):
        res[i, (full-i):(shape[1] // 2)] = 1
        res[i, ((shape[1] // 2) + 1):(shape[1] - (full-i))] = -1
    # res[2*shape[0]//3:, ((shape[1] // 2) + 1):] = -1
    
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.fliplr(get_motor_left_matrix(shape))
    return res
