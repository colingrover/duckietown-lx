from typing import Tuple


def DT_TOKEN() -> str:
    # TODO: change this to your duckietown token
    dt_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    return dt_token


def MODEL_NAME() -> str:
    # TODO: change this to your model's name that you used to upload it on google colab.
    # if you didn't change it, it should be "yolov5n"
    return "yolov5n"


def NUMBER_FRAMES_SKIPPED() -> int:
    # TODO: change this number to drop more frames
    # (must be a positive integer)
    return 3


def filter_by_classes(pred_class: int) -> bool:
    """
    Remember the class IDs:

        | Object    | ID    |
        | ---       | ---   |
        | Duckie    | 0     |
        | Cone      | 1     |
        | Truck     | 2     |
        | Bus       | 3     |


    Args:
        pred_class: the class of a prediction
    """
    # Right now, this returns True for every object's class
    # TODO: Change this to only return True for duckies!
    # In other words, returning False means that this prediction is ignored.
    return (pred_class == 0)


def filter_by_scores(score: float) -> bool:
    """
    Args:
        score: the confidence score of a prediction
    """
    # Right now, this returns True for every object's confidence
    # TODO: Change this to filter the scores, or not at all
    # (returning True for all of them might be the right thing to do!)
    return True


def filter_by_bboxes(bbox: Tuple[int, int, int, int]) -> bool:
    """
    Args:
        bbox: is the bounding box of a prediction, in xyxy format
                This means the shape of bbox is (leftmost x pixel, topmost y, rightmost x, bottommost y)
    """
    # TODO: Like in the other cases, return False if the bbox should not be considered.
    retVal = True
    imDim = 416

    leftmostX, topmostY, rightmostX, bottommostY = bbox # Unpack the tuple

    if (bottommostY < 5*imDim/6): # If bounding box isn't in lower sixth of image, it may be ignorable
        if (abs(bottommostY - topmostY) + abs(rightmostX-leftmostX) < 100): # Small ==> far away... ignore
            retVal = False
        elif (bottommostY < 2*imDim/3 or rightmostX < imDim/10 or leftmostX > (9*imDim)/10): # Ignore boxes contained on far sides or in upper 2 thirds
            retVal = False

    return retVal
