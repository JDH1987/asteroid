# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable,)

	# spawn player in middle of the screen
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# Create a new `AsteroidField` object in the initialization code.
	asteroid_field = AsteroidField()

	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		# call the player's update method
		updateable.update(dt)

		# fill the screen with black
		screen.fill("black")

		for asteroid in asteroids:
			if player.check_collision(asteroid):
				print("GAME OVER!")
				pygame.quit()
				exit()

		# draw the player
		for obj in drawable:
			obj.draw(screen)

		# flip the screen
		pygame.display.flip()

		# cap the frame rate to 60 FPS
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
