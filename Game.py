import pygame
import sys
import os

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pizza Designer with Images")

# Load images
def load_image(name):
    path = os.path.join("assets", name)
    return pygame.image.load(path).convert_alpha()

pizza_base = load_image("pizza_base.png")  # Optional: a pizza base image
pizza_rect = pizza_base.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Toppings list
toppings = [
    {"image": load_image("pepperoni.png"), "pos": [100, 100], "dragging": False},
    {"image": load_image("mushroom.png"), "pos": [150, 100], "dragging": False},
    {"image": load_image("olive.png"), "pos": [200, 100], "dragging": False},
]

clock = pygame.time.Clock()

def draw_pizza():
    screen.blit(pizza_base, pizza_rect)

def draw_toppings():
    for topping in toppings:
        screen.blit(topping["image"], topping["pos"])

def is_mouse_on_topping(topping, mouse_pos):
    rect = topping["image"].get_rect(topleft=topping["pos"])
    return rect.collidepoint(mouse_pos)

# Game loop
while True:
    screen.fill((255, 255, 255))
    draw_pizza()
    draw_toppings()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for topping in toppings:
                if is_mouse_on_topping(topping, event.pos):
                    topping["dragging"] = True

        elif event.type == pygame.MOUSEBUTTONUP:
            for topping in toppings:
                topping["dragging"] = False

        elif event.type == pygame.MOUSEMOTION:
            for topping in toppings:
                if topping["dragging"]:
                    topping["pos"] = list(event.pos)

    pygame.display.flip()
    clock.tick(60)
    # Button setup
font = pygame.font.SysFont(None, 40)
bake_button = pygame.Rect(WIDTH - 150, HEIGHT - 70, 120, 50)
baked = False
def draw_bake_button():
    pygame.draw.rect(screen, (200, 100, 50), bake_button)
    text = font.render("Bake", True, (255, 255, 255))
    screen.blit(text, (bake_button.x + 25, bake_button.y + 10))
    if baked:import pygame
import sys
import os

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pizza Designer with Images")

# Load images
def load_image(name):
    path = os.path.join("assets", name)
    return pygame.image.load(path).convert_alpha()

pizza_base = load_image("pizza_base.png")  # Optional: a pizza base image
pizza_rect = pizza_base.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Toppings list
toppings = [
    {"image": load_image("pepperoni.png"), "pos": [100, 100], "dragging": False},
    {"image": load_image("mushroom.png"), "pos": [150, 100], "dragging": False},
    {"image": load_image("olive.png"), "pos": [200, 100], "dragging": False},
]

clock = pygame.time.Clock()

def draw_pizza():
    screen.blit(pizza_base, pizza_rect)

def draw_toppings():
    for topping in toppings:
        screen.blit(topping["image"], topping["pos"])

def is_mouse_on_topping(topping, mouse_pos):
    rect = topping["image"].get_rect(topleft=topping["pos"])
    return rect.collidepoint(mouse_pos)

# Game loop
while True:
    screen.fill((255, 255, 255))
    draw_pizza()
    draw_toppings()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for topping in toppings:
                if is_mouse_on_topping(topping, event.pos):
                    topping["dragging"] = True

        elif event.type == pygame.MOUSEBUTTONUP:
            for topping in toppings:
                topping["dragging"] = False

        elif event.type == pygame.MOUSEMOTION:
            for topping in toppings:
                if topping["dragging"]:
                    topping["pos"] = list(event.pos)

    pygame.display.flip()
    clock.tick(60)
    # Button setup
font = pygame.font.SysFont(None, 40)
bake_button = pygame.Rect(WIDTH - 150, HEIGHT - 70, 120, 50)
baked = False
def draw_bake_button():
    pygame.draw.rect(screen, (200, 100, 50), bake_button)
    text = font.render("Bake", True, (255, 255, 255))
    screen.blit(text, (bake_button.x + 25, bake_button.y + 10))
    if baked:
        baked_text = font.render("Baked!", True, (0, 200, 0))
        screen.blit(baked_text, (WIDTH - 150, HEIGHT - 120))
draw_bake_button()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if bake_button.collidepoint(event.pos):
            baked = True
        baked_text = font.render("Baked!", True, (0, 200, 0))
        screen.blit(baked_text, (WIDTH - 150, HEIGHT - 120))
draw_bake_button()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if bake_button.collidepoint(event.pos):
            baked = True