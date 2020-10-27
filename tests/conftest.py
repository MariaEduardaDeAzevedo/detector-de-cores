import pytest
import numpy as np


@pytest.fixture
def dummy_image():
    data = [
        [[120, 120, 120], [0, 0, 0], [0, 0, 0]],
        [[110, 110, 110], [140, 140, 140], [0, 0, 0]],
        [[200, 200, 200], [155, 155, 155], [150, 150, 150]],
    ]
    return np.array(data, dtype=np.uint8)
