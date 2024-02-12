from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")

    res[200:400, :(shape[1] // 2)] = 1
    res[200:400, ((shape[1] // 2) + 1):] = -1
    # res[2*shape[0]//3:, ((shape[1] // 2) + 1):] = -1
    
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.fliplr(get_motor_left_matrix(shape))
    return res
