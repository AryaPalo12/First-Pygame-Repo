import pygame 

screen_size = [360 , 600]

screen = pygame.display.set_mode(screen_size)

background = pygame.image.load('Assets/background.png')

planet = pygame.image.load ('Assets/one.png')

spaceship = pygame.image.load ('Assets/spaceship.png')

bullet = pygame.image.load ('Assets/bullet.png')
bullet_y = 500
fired = False

keep_alive = True
clock = pygame.time.Clock()
while keep_alive :
  pygame.event.get()
  keys =pygame.key.get_pressed()
  if keys[pygame.K_SPACE] == True :
    fired = True

  if fired == True :
    bullet_y = bullet_y - 5
    if bullet_y == 50 :
      fired = False
      bullet_y = 500
  screen.blit(background,[0,0])
  screen.blit(bullet,[180,bullet_y])
  screen.blit(spaceship,[160,500])

  """if move_direction == 'right':
    planet_x = planet"""

  pygame.display.update()
  clock.tick(60)
  screen.blit(planet,[140,50])
  
