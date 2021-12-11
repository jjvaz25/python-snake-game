import pygame
from pygame.locals import * #importing event keywords
import time #necessary for letting snake move on its own, but slowly


class Snake:
  def __init__(self, parent_screen):
    #draws the starting snake block on the background
    self.parent_screen = parent_screen
    self.block = pygame.image.load('resources/block.jpeg').convert()
    self.x = 100
    self.y = 100
    self.direction = 'down' #snake moves down upon initializing

  #function that draws snake block
  def draw(self):
    self.parent_screen.fill((110, 110, 5)) #erases old block so that it updates with each key hit
    self.parent_screen.blit(self.block, (self.x, self.y))
    pygame.display.flip()

  def move_left(self):
    self.direction = 'left'

  def move_right(self):
    self.direction = 'right'

  def move_up(self):
    self.direction = 'up'

  def move_down(self):
    self.direction = 'down'

  def walk(self):
    if self.direction == 'down':
      self.y +=10
    elif self.direction == 'up':
      self.y -=10
    elif self.direction == 'left':
      self.x -= 10
    else: #move right
      self.x += 10
    
    self.draw()


class Game:
  def __init__(self):
    pygame.init()

    #setting the window size and background of the main display
    self.surface = pygame.display.set_mode((500,500))
    self.surface.fill((110,110,5))
    self.snake = Snake(self.surface) #creates snake inside of game class
    self.snake.draw() 
  
  def run(self):
    #set loop to continue playing game until the escape or X button is hit
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            running = False
          
          #moving the snake based on arrow buttons hit
          if event.key == K_UP:
            self.snake.move_up()
          
          if event.key == K_DOWN:
            self.snake.move_down()
          
          if event.key == K_LEFT:
            self.snake.move_left()
          
          if event.key == K_RIGHT:
            self.snake.move_right()
        
        elif event.type == QUIT:
          running = False 
      
      self.snake.walk()
      time.sleep(0.2) #every 0.2 seconds snake moves


if __name__ == "__main__":
  game = Game()
  game.run()