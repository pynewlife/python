import pygame
class Ship():
    def __init__(self,ai_settings,screen):
       # 初始化飞机,并且对其进行设置
        self.screen = screen
        self.ai_settings = ai_settings
       # 加载飞船图像并且获取其外接举行
        self.image = pygame.image.load("images\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
       # 将每个新的飞船放到图像中心
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        #移动表示
        self.moving_right = False
        self.move_left = False
        # 飞船的速度设置

    def update(self):
        # 根据移动表示调整飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.move_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
        # 在指定的位置绘制飞船
        self.screen.blit(self.image,self.rect)
