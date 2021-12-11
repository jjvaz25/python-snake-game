import pygame
from pygame.locals import * #importing event keywords


class Snake:
  def __init__(self, parent_screen):
    #draws the starting snake block on the background
    self.parent_screen = parent_screen
    self.block = pygame.image.load('resources/block.jpeg').convert()
    self.x = 100
    self.y = 100

  #function that draws snake block
  def draw(self):
    self.parent_screen.fill((110, 110, 5)) #erases old block so that it updates with each key hit
    self.parent_screen.blit(self.block, (self.x, self.y))
    pygame.display.flip()

  def move_left(self):
    self.x -= 10
    self.draw()

  def move_right(self):
    self.x += 10
    self.draw()

  def move_up(self):
    self.y -=10
    self.draw()

  def move_down(self):
    self.y +=10
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



if __name__ == "__main__":
  game = Game()
  game.run()