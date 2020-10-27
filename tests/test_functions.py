import numpy as np
from detector_de_cores.functions import generate_mask


def test_generate_mask(dummy_image):
    max_hsv = [150, 150, 150]
    min_hsv = [120, 120, 120]
    expected_result = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]

    mask = generate_mask(max_hsv, min_hsv, dummy_image)
    np.alltrue(mask == expected_result)
