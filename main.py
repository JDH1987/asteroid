# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():

	pygame.init()

	clock = pygame.time.Clock()
	dt = 0

	# spawn player in middle of the screen
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		# fill the screen with clack
		screen.fill((0, 0, 0))

		# draw the player
		player.draw(screen)

		# flip the screen
		pygame.display.flip()

		# cap the frame rate
		dt = clock.tick(60) / 1000


	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
