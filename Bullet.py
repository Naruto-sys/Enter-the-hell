import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, damage, speed, start_pos, point_pos, distance, walls):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = start_pos[0]
        self.rect.y = start_pos[1]

        self.walls = walls

        self.damage = damage
        self.speed = speed
        self.distance = distance

        self.start_pos = start_pos
        self.x = self.start_pos[0] - point_pos[0]
        self.y = self.start_pos[1] - point_pos[1]

        self.point_pos = point_pos
        x1 = self.point_pos[0] - self.start_pos[0]
        y1 = self.point_pos[1] - self.start_pos[1]

        while (x1 ** 2 + y1 ** 2) ** 0.5 < 600:
            x1 += self.x / self.speed
            y1 += self.y / self.speed

        self.x = int(x1)
        self.y = int(y1)

    def update(self, *args):
        self.rect.x -= self.x // self.speed
        self.rect.y -= self.y // self.speed

        if self.x < 0:
            if self.rect.x < self.x + self.start_pos[0]:
                self.kill()
        if self.x > 0:
            if self.rect.x > self.x + self.start_pos[0]:
                self.kill()
        for elem in self.walls:
            if pygame.sprite.collide_mask(self, elem):
                self.kill()