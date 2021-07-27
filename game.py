import pygame, sys, random

from pygame.transform import rotate

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900)) # 2 floor

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True) # X, Y
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            print('collision')
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        print('collision')
        return False

    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement *3, 1)
    return new_bird


pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

# Game Var
gravity = 0.25
bird_movement = 0

game_active = True



bg_surface = pygame.image.load('assets/background-day.png').convert() # Make faster
bg_surface = pygame.transform.scale2x(bg_surface) # X2

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100,512))


# bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
# bird_surface = pygame.transform.scale2x(bird_surface)
# bird_rect = bird_surface.get_rect(center = (100, 512))

pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)

pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200) #1.2
pipe_height = [400, 600, 800]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                # print("flat")
                bird_movement = 0
                bird_movement -= 6

            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 512)
                bird_movement = 0


        
        if event.type == SPAWNPIPE:
            # print('pipe')
            pipe_list.extend(create_pipe())
            # print(pipe_list)
    screen.blit(bg_surface, (0,0))

    if game_active:
        #bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)



    # Floor
    floor_x_pos -= 1
    # screen.blit(floor_surface, (floor_x_pos, 900))
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    

    pygame.display.update()
    clock.tick(120)