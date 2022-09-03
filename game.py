import pygame


class Dino(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (400, 400))
        self.x = player_x
        self.y = player_y
        self.isJump = False
        self.jumpCount = 10

    def reset(self):
        screen.blit(self.image, (self.x, self.y))

    def jump(self):
        keys_pressed = pygame.key.get_pressed()
        if not self.isJump:
            if keys_pressed[pygame.K_SPACE]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False


BLACK = (0, 0, 0)
FPS = 40
win_width = 800
win_height = 500

dino = Dino("images/dino.png", 70, 180)
cactus = pygame.transform.scale(pygame.image.load("images/cactus.png"), (100, 100))
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Dino")
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    screen.blit(cactus, (500, 300))
    pygame.draw.rect(screen, (255, 255, 255), (0, 400, 800, 10))
    dino.jump()
    dino.reset()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
