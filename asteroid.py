import pygame
<<<<<<< HEAD
<<<<<<< HEAD

<<<<<<< HEAD
import random
=======
>>>>>>> a3d3fc2 (Added Asteroids (or space bubbles))
from constants import *
=======
>>>>>>> 5d2b3b1 (Added shooting. Cleaned up code to match solution files)
=======

import random
from constants import *
>>>>>>> 676c1dc (The big asteroids break into smaller asteroids when a bullet collides with it)
from circleshape import CircleShape

class Asteroid(CircleShape):
<<<<<<< HEAD
<<<<<<< HEAD
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
<<<<<<< HEAD

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):

		self.kill()

		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			random_angle = random.uniform(20, 50)
			new_velocity1 = self.velocity.rotate(random_angle)
			new_velocity2 = self.velocity.rotate(-random_angle)

			new_radius = self.radius - ASTEROID_MIN_RADIUS

			asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

			asteroid1.velocity = new_velocity1 * 1.2
			asteroid2.velocity = new_velocity2 * 1.2
=======
		self.radius = radius
=======
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
>>>>>>> 5d2b3b1 (Added shooting. Cleaned up code to match solution files)
=======
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
>>>>>>> 676c1dc (The big asteroids break into smaller asteroids when a bullet collides with it)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

<<<<<<< HEAD
<<<<<<< HEAD
	def update(self, dt):
		self.position += self.velocity * dt
>>>>>>> a3d3fc2 (Added Asteroids (or space bubbles))
=======
    def update(self, dt):
        self.position += self.velocity * dt
>>>>>>> 5d2b3b1 (Added shooting. Cleaned up code to match solution files)
=======
	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):

		self.kill()

		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			random_angle = random.uniform(20, 50)
			new_velocity1 = self.velocity.rotate(random_angle)
			new_velocity2 = self.velocity.rotate(-random_angle)

			new_radius = self.radius - ASTEROID_MIN_RADIUS

			asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

			asteroid1.velocity = new_velocity1 * 1.2
			asteroid2.velocity = new_velocity2 * 1.2
>>>>>>> 676c1dc (The big asteroids break into smaller asteroids when a bullet collides with it)
