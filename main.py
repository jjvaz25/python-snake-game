import pygame
from pygame.locals import * #importing event keywords

#function that draws snake block
def draw_block():
  surface.fill((110, 110, 5)) #erases old block so that it updates with each key hit
  surface.blit(block, (block_x, block_y))
  pygame.display.flip()

if __name__ == "__main__":
  pygame.init()

  #setting the window size and background of the main display
  surface = pygame.display.set_mode((500,500))
  surface.fill((110,110,5))

  #draws the snake block on the background
  block = pygame.image.load('resources/block.jpeg').convert()
  block_x = 100
  block_y = 100
  surface.blit(block, (block_x, block_y))

  pygame.display.flip()

  #set loop to continue playing game until the escape or X button is hit
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          running = False
        
        #moving the snake based on arrow buttons hit
        if event.key == K_UP:
          block_y -= 10
          draw_block()
        if event.key == K_DOWN:
          block_y += 10
          draw_block()
        if event.key == K_LEFT:
          block_x -= 10
          draw_block()
        if event.key == K_RIGHT:
          block_x += 10
          draw_block()
      
      elif event.type == QUIT:
        running = False 

