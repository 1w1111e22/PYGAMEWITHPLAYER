import pygame


class Player:
    def __init__(self, image_path, width=50, height=50, x=0, y=0):
        self.image_path = image_path
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # Загрузка и масштабирование изображения
        self.surface = pygame.image.load(image_path)
        self.surface = pygame.transform.scale(self.surface, (self.width, self.height))

        # Получение прямоугольника для отслеживания позиции
        self.rect = self.surface.get_rect(center=(x, y))

    def draw(self, screen):
        # Отрисовка изображения на экране
        screen.blit(self.surface, (self.x - self.width // 2, self.y - self.height // 2))