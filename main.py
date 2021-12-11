import pygame
from pygame.locals import * #importing event keywords
import time #necessary for letting snake move on its own, but slowly

SIZE = 40 #the size of each block that makes up the snake


class Apple:
  def __init__(self, parent_screen):
    self.image = pygame.image.load('resources/apple.jpeg').convert()
    self.parent_screen = parent_screen #so that the apple can be painted
    self.x = SIZE * 3
    self.y = SIZE * 3
  
  def draw(self):
    self.parent_screen.blit(self.image, (self.x, self.y))
    pygame.display.flip()


class Snake:
  def __init__(self, parent_screen, length):
    #draws the starting snake block on the background
    self.parent_screen = parent_screen #allows snake to be painted
    self.length = length
    self.block = pygame.image.load('resources/block.jpeg').convert()
    self.x = [SIZE] * length
    self.y = [SIZE] * length
    self.direction = 'down' #snake moves down upon initializing

  #function that draws snake block to its new position
  def draw(self):
    self.parent_screen.fill((110, 110, 5)) #erases old block so that it updates with each key hit
    
    #drawn snake based on its length
    for i in range(self.length):
      self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
    
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

    #adding functionality to that the latter blocks of the snake move into the place
    # of the block in front of them
    for i in range(self.length - 1, 0, -1): #(starting list val, ending list val, step size)
      self.x[i] = self.x[i - 1]
      self.y[i] = self.y[i - 1]

    if self.direction == 'down':
      self.y[0] += SIZE # keeps the blocks 40px apart
    elif self.direction == 'up':
      self.y[0] -= SIZE
    elif self.direction == 'left':
      self.x[0] -= SIZE
    else: #move right
      self.x[0] += SIZE
    
    self.draw()


class Game:
  def __init__(self):
    pygame.init()

    #setting the window size and background of the main display
    self.surface = pygame.display.set_mode((1000,800))
    self.surface.fill((110,110,5))
    self.snake = Snake(self.surface, 6) #creates snake inside of game class
    self.snake.draw() 
    self.apple = Apple(self.surface)
    self.apple.draw()
  
  def is_collision(self, x1, x2, y1, y2):
    if x1 >= x2 + SIZE and x1 <= x2 + SIZE:
      if y1 >= x2 + SIZE and y1 <= x2 + SIZE:
        return True
    return False



  def play(self):
    self.snake.walk()
    self.apple.draw()

    if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
      print('collision occured')

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
      
      self.play()
      time.sleep(0.3) #every 0.3 seconds snake moves, needed it to slow down


if __name__ == "__main__":
  game = Game()
  game.run()