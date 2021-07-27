import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900)) # 2 floor
    

pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background-day.png').convert() # Make faster
bg_surface = pygame.transform.scale2x(bg_surface) # X2

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('assets/')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0,0))
    floor_x_pos -= 1
    # screen.blit(floor_surface, (floor_x_pos, 900))
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    

    pygame.display.update()
    clock.tick(120)