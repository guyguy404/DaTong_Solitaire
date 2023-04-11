import pygame
import numpy as np
from pygame import Surface

def darken(surface: Surface, ratio: float=0.5) -> None:
    """将一个Surface的图像变暗"""
    if ratio < 0 or ratio > 1:
        raise Exception("darken func: ratio can only be 0-1")
    array = pygame.surfarray.array3d(surface)
    array = (array * ratio).astype(np.uint8)
    pygame.surfarray.blit_array(surface, array)
    del array