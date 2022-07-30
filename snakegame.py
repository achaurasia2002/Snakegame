import pygame
pygame.init()

#colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#creating window
screen_width = 1200
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#set game title
pygame.display.set_caption("SnakeGame")
pygame.display.upadate()

# Game variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 10
velocity_y = 10
snake_size = 10
fps = 30

clock = pygame.time.clock()
#game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10

            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 10

            if event.key == pygame.K_UP:
                snake_x = snake_y - 10

            if event.key == pygame.K_DOWN:
                snake_x = snake_y + 10 

snake_x = snake_x + velocity_x
snake_y = snake_y + velocity_y                           


gameWindow.fill(white) 
pygame.draw.react(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
pygame.display.update()
clock.tick(fps)



pygame.quit()
quit()

