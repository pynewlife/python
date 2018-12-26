import sys
import pygame
from ship import Ship
from settings import Settings
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化一个游戏窗口
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("飞机大战")
    # 设置背景色
    bg_color = (200,200,200)
    # 开始游戏主循环
    ship = Ship(ai_settings,screen)
    #创建一个子弹的编组
    bullets = Group()
    while True:
        # 检测鼠标和键盘事件
        gf.check_events(ai_settings,screen,ship,bullets)
        # 刷新飞船状态
        ship.update()
        #刷新子弹状态
        bullets.update()
        # 让最近绘制的屏幕可见
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()

