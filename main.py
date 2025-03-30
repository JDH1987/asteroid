# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():

	pygame.init()

	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	Player.containers = (updateable, drawable)

	clock = pygame.time.Clock()
	dt = 0

	# spawn player in middle of the screen
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		# call the player's update method
		updateable.update(dt)

		# fill the screen with black
		screen.fill((0, 0, 0))

		# draw the player
		for entity in drawable:
			entity.draw(screen)

		# flip the screen
		pygame.display.flip()

		# cap the frame rate
		dt = clock.tick(60) / 1000


	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
