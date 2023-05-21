import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela do jogo
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids")

# Definição das cores
WHITE = (255, 255, 255)

# Classe da nave
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("gato.jpg")
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Classe do meteoro
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("gato.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 3)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > height + 10:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 3)

# Classe da bala
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("gato.jpg")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

# Criação dos grupos de sprites
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Criação da nave
ship = Ship()
all_sprites.add(ship)

# Criação dos asteroides
for _ in range(8):
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    # Controle de FPS
    clock.tick(30)

    # Eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()

    # Atualização dos sprites
    all_sprites.update()

    # Colisões entre a bala e os asteroides
    hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
    for hit in hits:
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroids.add(asteroid)

    # Colisões entre a nave e os asteroides
    hits = pygame.sprite.spritecollide(ship, asteroids, False)
    if hits:
        running = False

    # Preenchimento do fundo
    screen.fill(WHITE)

    # Desenho dos sprites na tela
    all_sprites.draw(screen)

    # Atualização da tela
    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()
