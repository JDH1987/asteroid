<<<<<<< HEAD
<<<<<<< HEAD
=======
# this allows us to use code from
# the open-source pygame library
# throughout this file
>>>>>>> fbfcefc (Cleaned up code)
=======
>>>>>>> 5d2b3b1 (Added shooting. Cleaned up code to match solution files)
import sys
import pygame
from constants import *
from player import Player
<<<<<<< HEAD
<<<<<<< HEAD
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

<<<<<<< HEAD
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
=======

def main():
<<<<<<< HEAD
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
>>>>>>> 5d2b3b1 (Added shooting. Cleaned up code to match solution files)
=======
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
>>>>>>> 2342a67 (Added destruction of asteroids. (Or popping of space bubbles))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()

	Player.containers = (updatable, drawable)

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
>>>>>>> 5d2b3b1 (Added shooting. Cleaned up code to match solution files)
=======
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
>>>>>>> 2342a67 (Added destruction of asteroids. (Or popping of space bubbles))

	dt = 0

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 84804ef (Drew a player triangle)
=======
>>>>>>> 2342a67 (Added destruction of asteroids. (Or popping of space bubbles))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
<<<<<<< HEAD

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
<<<<<<< HEAD
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

<<<<<<< HEAD
		# fill the screen with black
<<<<<<< HEAD
>>>>>>> 7a88baa (Added WASD movement and turning)
		screen.fill((0, 0, 0))
=======
		screen.fill("black")
>>>>>>> 689842b (Cleaned up code)

=======
>>>>>>> fbfcefc (Cleaned up code)
		for asteroid in asteroids:
			if player.check_collision(asteroid):
				print("GAME OVER!")
				sys.exit()
=======
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
=======
>>>>>>> 2342a67 (Added destruction of asteroids. (Or popping of space bubbles))

		updatable.update(dt)

<<<<<<< HEAD
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
>>>>>>> 5d2b3b1 (Added shooting. Cleaned up code to match solution files)
=======
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()
>>>>>>> 2342a67 (Added destruction of asteroids. (Or popping of space bubbles))

		for asteroid in asteroids:
			for shot in shots:
				if shot.collides_with(asteroid):
					asteroid.kill()
=======
>>>>>>> 676c1dc (The big asteroids break into smaller asteroids when a bullet collides with it)
					shot.kill()

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000


<<<<<<< HEAD
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

=======
>>>>>>> 689842b (Cleaned up code)
if __name__ == "__main__":
<<<<<<< HEAD
    main()
>>>>>>> a20eba5 (Initial commit with basic game loop)
=======
	main()
>>>>>>> 2342a67 (Added destruction of asteroids. (Or popping of space bubbles))
