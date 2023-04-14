import pygame
from pygame import Surface, Rect
from pygame.sprite import Sprite
from settings import Settings
from button import Button

class Window(Sprite):
    """游戏中所有弹出窗口的基类"""
    