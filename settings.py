class Settings:
    """存储游戏中所有设置的类"""
    
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
    hand_card_spacing = 0.5 * hand_card_width
    suits = ['spade', 'club', 'heart', 'diamond']