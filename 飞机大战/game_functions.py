import sys
import pygame
from bullet import Bullet

#
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    # 构造检测键盘按下的响应函数
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    # 创建一颗子弹加入到编组中
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
def check_keyup_events(event,ship):
    # 构造检测键盘按键抬起的函数
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
def update_screen(ai_settings,screen,ship,bullets):
    # 在飞船和外星人的后边绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
