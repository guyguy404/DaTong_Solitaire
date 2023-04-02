import sys
import pygame

from settings import Settings

class DaTongSolitaire:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("大通纸牌")
        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        
        pygame.display.flip()
        
        
if __name__ == '__main__':
    dts = DaTongSolitaire()
    dts.run_game()