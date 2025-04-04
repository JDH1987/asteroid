import pygame
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5d2b3b1 (Added shooting. Cleaned up code to match solution files)
from constants import *
from circleshape import CircleShape
from shot import Shot

<<<<<<< HEAD
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
=======

class Player(CircleShape):
<<<<<<< HEAD
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
>>>>>>> 5d2b3b1 (Added shooting. Cleaned up code to match solution files)
=======
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shoot_timer = 0
>>>>>>> e7c7e1f (Added shooting)

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
>>>>>>> 5d2b3b1 (Added shooting. Cleaned up code to match solution files)
=======
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
>>>>>>> e7c7e1f (Added shooting)

	def update(self, dt):

		self.shoot_timer -= dt
		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			self.move(dt)

		if keys[pygame.K_s]:
			self.move(-dt)

<<<<<<< HEAD
<<<<<<< HEAD
		if keys[pygame.K_w]:
			self.move(dt)

		if keys[pygame.K_s]:
			self.move(-dt)
=======
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
>>>>>>> e7c7e1f (Added shooting)

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
<<<<<<< HEAD
>>>>>>> 7a88baa (Added WASD movement and turning)
=======
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
>>>>>>> 5d2b3b1 (Added shooting. Cleaned up code to match solution files)
=======
>>>>>>> e7c7e1f (Added shooting)
