import sys
import pygame
from constants import *
from player import Player
<<<<<<< HEAD
<<<<<<< HEAD
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

=======
>>>>>>> 84804ef (Drew a player triangle)
=======
from asteroid import Asteroid
from asteroidfield import AsteroidField
>>>>>>> a3d3fc2 (Added Asteroids (or space bubbles))

def main():
	pygame.init()
<<<<<<< HEAD
<<<<<<< HEAD
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
=======
=======
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
>>>>>>> 689842b (Cleaned up code)

	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable,)

<<<<<<< HEAD
>>>>>>> f44bf00 (Added groups instead of calling methods directly)
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()

	Player.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	dt = 0

<<<<<<< HEAD
=======
=======
>>>>>>> 689842b (Cleaned up code)
	# spawn player in middle of the screen
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# Create a new `AsteroidField` object in the initialization code.
	asteroid_field = AsteroidField()

	dt = 0

>>>>>>> 84804ef (Drew a player triangle)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
		updatable.update(dt) # type: ignore

		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()

		for asteroid in asteroids:
			for shot in shots:
				if shot.collides_with(asteroid):
					asteroid.split()
					shot.kill()

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
=======
=======
=======
		# fill the screen with clack
>>>>>>> 84804ef (Drew a player triangle)
=======
		# call the player's update method
		updateable.update(dt)

		# fill the screen with black
<<<<<<< HEAD
>>>>>>> 7a88baa (Added WASD movement and turning)
		screen.fill((0, 0, 0))
=======
		screen.fill("black")
>>>>>>> 689842b (Cleaned up code)

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

<<<<<<< HEAD
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

=======
>>>>>>> 689842b (Cleaned up code)
if __name__ == "__main__":
    main()
>>>>>>> a20eba5 (Initial commit with basic game loop)
