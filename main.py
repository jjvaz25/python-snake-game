import pygame
from pygame.locals import * #importing event keywords
import time #necessary for letting snake move on its own, but slowly
import random #necessary to randomly move apple after eating

SIZE = 40 #the size of each block that makes up the snake
BACKGROUND_COLOR = (110, 110, 5)

class Apple:
  def __init__(self, parent_screen):
    self.image = pygame.image.load('resources/apple.jpeg').convert()
    self.parent_screen = parent_screen #so that the apple can be painted
    self.x = SIZE * 3
    self.y = SIZE * 3
  
  def draw(self):
    self.parent_screen.blit(self.image, (self.x, self.y))
    pygame.display.flip()

  def move(self):
    self.x = random.randint(1,24) * SIZE
    self.y = random.randint(1,19) * SIZE

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
    self.parent_screen.fill((BACKGROUND_COLOR)) #erases old block so that it updates with each key hit
    
    #drawn snake based on its length
    for i in range(self.length):
      self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
    
    pygame.display.flip()

  def increase_length(self):
    self.length += 1
    self.x.append(-1)
    self.y.append(-1)

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
    self.surface.fill((BACKGROUND_COLOR))
    self.snake = Snake(self.surface, 5) #creates snake inside of game class
    self.snake.draw() 
    self.apple = Apple(self.surface)
    self.apple.draw()
  
  def is_collision(self, x1, y1, x2, y2):
    if x1 >= x2 and x1 < x2 + SIZE:
      if y1 >= y2 and y1 < y2 + SIZE:
        return True
    return False

  def display_score(self):
    font = pygame.font.SysFont('arial', 30)
    score = font.render(f'Score: {self.snake.length}', True, (255, 255, 255))
    self.surface.blit(score, (800, 10)) #any time you want something to display on the game, you need to use surface and blit


  def play(self):
    self.snake.walk()
    self.apple.draw()
    self.display_score()
    pygame.display.flip()

    #snake colliding with apple
    if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y): 
      self.snake.increase_length()
      self.apple.move()
      print('collision occured')

    #snake eating/colliding with itself
    for i in range(2, self.snake.length): #snake can't collide with 0 or 1
      if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]): 
        raise 'Game Over!'
        print('game over')

  def show_game_over(self):
    self.surface.fill((BACKGROUND_COLOR))
    font = pygame.font.SysFont('arial', 30)
    line1 = font.render(f'Game Over! Score: {self.snake.length}', True, (255, 255, 255))
    self.surface.blit(line1, (200,300))
    line2 = font.render(f'To play again hit ENTER. To exit press Escape', True, (255, 255, 255))
    self.surface.blit(line2, (200,350))
    pygame.display.flip() #refreshes the UI

  def reset(self):
    self.snake = Snake(self.surface, 1)
    self.apple = Apple(self.surface)

  def run(self):
    #set loop to continue playing game until the escape or X button is hit
    running = True
    pause = False
    while running:
      for event in pygame.event.get():
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            running = False
          
          if event.key == K_RETURN:
            pause = False

          #moving the snake based on arrow buttons hit
          if not pause: 
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
      
      try: 
        if not pause:  
          self.play()
      except Exception as e:
        self.show_game_over()
        pause = True
        self.reset()
      
      time.sleep(0.1) #every 0.3 seconds snake moves, needed it to slow down
      


if __name__ == "__main__":
  game = Game()
  game.run()