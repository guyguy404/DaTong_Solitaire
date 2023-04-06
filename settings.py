import pygame

class Settings:
    """存储游戏中所有设置的类"""
    # 中文字体
    font = '霞鹜文楷'
    font_path = pygame.font.match_font(font)
    
    # 屏幕设置
    screen_width = 1200
    screen_height = 800
    bg_color = (105, 139, 105)
    
    # 卡牌相关设置
    card_width = 500
    card_height = 726
    load_card_scale = 0.3
    hand_card_width = load_card_scale * card_width
    hand_card_height = load_card_scale * card_height
    hand_card_x_spacing = 0.5 * hand_card_width
    hand_card_y_spacing = 0.25 * hand_card_height
    suits = ['spade', 'club', 'heart', 'diamond']
    playable_card_frame_color = (255, 0, 0)
    playable_card_frame_width = 15
    playable_card_frame_border_radius = 7    # 边框圆角的半径
    
    # 场地设置
    field_x_spacing = screen_width // 6
    field_x_margin = int(field_x_spacing * 1.5)
    field_y_spacing = hand_card_y_spacing
    
    # 信息面板设置
    board_width = 200
    board_height = 250
    board_x_margin = 90
    board_y_margin = 20
    board_color = (205, 170, 125)
    board_font_size = 20
    board_text_left_margin = 20
    board_text_top_margin = 20
    board_text_line_spacing = 10
    
    # 分数设置
    base_score = [6, -1, -2, -3]

    def init():
        Settings.field_x_spacing = Settings.screen_width // 6
        Settings.field_x_margin = int(Settings.field_x_spacing * 1.5)
        Settings.field_y_spacing = Settings.hand_card_y_spacing