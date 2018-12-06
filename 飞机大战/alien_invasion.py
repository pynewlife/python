import sys
import pygame
from ship import Ship
from settings import Settings
import game_functions as gf


def run_game():
    # 初始化一个游戏窗口
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("alien Invasion")
    # 设置背景色
    bg_color = (230,230,230)
    # 开始游戏主循环
    ship = Ship(ai_settings,screen)
    while True:
        gf.check_events(ship)
        ship.update()
        # 检测鼠标和键盘事件
        gf.check_events(ship)
        # 让最近绘制的屏幕可见
        gf.update_screen(ai_settings,screen,ship)
run_game()

