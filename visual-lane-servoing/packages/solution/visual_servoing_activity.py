from typing import Tuple

import numpy as np
import cv2


def get_steer_matrix_left_lane_markings(shape: Tuple[int, int]) -> np.ndarray:
    """
    Args:
        shape:              The shape of the steer matrix.

    Return:
        steer_matrix_left:  The steering (angular rate) matrix for Braitenberg-like control
                            using the masked left lane markings (numpy.ndarray)
    """

    # TODO: implement your own solution here
    steer_matrix_left = np.zeros(shape)
    steer_matrix_left[:, :shape[1]//2] = 1 # Right half only
    # ---
    return steer_matrix_left


def get_steer_matrix_right_lane_markings(shape: Tuple[int, int]) -> np.ndarray:
    """
    Args:
        shape:               The shape of the steer matrix.

    Return:
        steer_matrix_right:  The steering (angular rate) matrix for Braitenberg-like control
                             using the masked right lane markings (numpy.ndarray)
    """

    # TODO: implement your own solution here
    steer_matrix_left = np.zeros(shape)
    steer_matrix_left[:, (shape[1]//2):] = 1 # Left half only
    # ---
    return steer_matrix_right


def detect_lane_markings(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Args:
        image: An image from the robot's camera in the BGR color space (numpy.ndarray)
    Return:
        mask_left_edge:   Masked image for the dashed-yellow line (numpy.ndarray)
        mask_right_edge:  Masked image for the solid-white line (numpy.ndarray)
    """
    h, w, _ = image.shape

    white_lower_hsv = np.array([0, 0, 150])
    white_upper_hsv = np.array([179, 45, 255])
    yellow_lower_hsv = np.array([20, 115, 166])
    yellow_upper_hsv = np.array([28, 255, 240])

    # Convert the image to HSV for any color-based filtering
    imghsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask_right_edge = cv2.inRange(imghsv, white_lower_hsv, white_upper_hsv)
    mask_left_edge = cv2.inRange(imghsv, yellow_lower_hsv, yellow_upper_hsv)

    return mask_left_edge, mask_right_edge
