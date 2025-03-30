import pygame
<<<<<<< HEAD
<<<<<<< HEAD
from constants import *
from circleshape import CircleShape
from shot import Shot

=======
from constants import PLAYER_RADIUS
=======
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
>>>>>>> 7a88baa (Added WASD movement and turning)
from circleshape import CircleShape
>>>>>>> 84804ef (Drew a player triangle)

class Player(CircleShape):
	def __init__(self, x, y):
<<<<<<< HEAD
		super().__init__(x, y, PLAYER_RADIUS)
<<<<<<< HEAD
		self.rotation = 0
		self.shoot_timer = 0

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def update(self, dt):

		self.shoot_timer -= dt
		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			self.move(dt)

		if keys[pygame.K_s]:
			self.move(-dt)

		if keys[pygame.K_a]:
			self.rotate(-dt)

		if keys[pygame.K_d]:
			self.rotate(dt)

		if keys[pygame.K_SPACE]:
			self.shoot()

	def shoot(self):
		if self.shoot_timer > 0:
			return
		self.shoot_timer = PLAYER_SHOOT_COOLDOWN
		shot = Shot(self.position.x, self.position.y)
		shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
=======
		self.position = pygame.Vector2(x, y)
		self.rotation = 0
=======
		super().__init__(x, y, PLAYER_RADIUS) # call parent class constructor
		self.rotation = 0 # initialize the rotation
>>>>>>> 7a88baa (Added WASD movement and turning)

	# in the player class
	def triangle(self):
    		forward = pygame.Vector2(0, 1).rotate(self.rotation)
    		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    		a = self.position + forward * self.radius
    		b = self.position - forward * self.radius - right
    		c = self.position - forward * self.radius + right
    		return [a, b, c]

	def draw(self, screen):
<<<<<<< HEAD
<<<<<<< HEAD
		points = self.triangle()
		pygame.draw.polygon(screen, "white", points, 2)
>>>>>>> 84804ef (Drew a player triangle)
=======
		points = self.triangle() # get the points of the triangle
		pygame.draw.polygon(screen, "white", points, 2) # draw the triangle
=======
		pygame.draw.polygon(screen, "white", self.triangle(), 2) # draw the triangle
>>>>>>> 689842b (Cleaned up code)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt # rotate based on turn speed

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt)

		if keys[pygame.K_d]:
			self.rotate(dt)

		if keys[pygame.K_w]:
			self.move(dt)

		if keys[pygame.K_s]:
			self.move(-dt)

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
>>>>>>> 7a88baa (Added WASD movement and turning)
