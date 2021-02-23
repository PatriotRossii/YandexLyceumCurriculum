import pygame

pygame.init()

w = 300
h = 200

screen = pygame.display.set_mode((w, h))
screen.fill(pygame.Color(255, 255, 255))

brick_color = pygame.Color(255, 0, 0)

for i, pos_x in enumerate(range(0, w, 15)):
    for j, pos_y in enumerate(range(0, h, 17)):
        pygame.draw.rect(screen, brick_color, pygame.Rect((pos_x + i * 17) - (15 if j % 2 else 0), pos_y, 30, 15))

pygame.display.flip()

pygame.display.set_caption("Крест")

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()