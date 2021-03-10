import shutil

import requests
import pygame

X = 450
Y = 450

points = [("2.295106,48.858360", 17), ("15.383912,43.978569", 15),
          ("-116.866567,37.401790", 17), ("109.179067,19.668193", 14)]
images = []

for i, point in enumerate(points):
    response = requests.get(f"https://static-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&"
                            f"l=sat&ll={point[0]}&z={point[1]}", stream=True)

    image_name = f"image{i}.png"
    images.append(image_name)

    with open(image_name, "wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)

pygame.init()

white = (255, 255, 255)

display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Слайд-шоу')

current_image = 0

image = pygame.image.load(images[current_image % len(images)])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            current_image += 1

            image = pygame.image.load(images[current_image % len(images)])
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.display.update()
