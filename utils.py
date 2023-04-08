import pygame
from pygame import Surface

def darken(surface: Surface):
    """将一个Surface的图像变暗"""
    pixels = pygame.surfarray.pixels3d(surface)
    pixels //= 2
    del pixels