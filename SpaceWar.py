#Simple Turtle Graphics Game

import random
import winsound
from tkinter import messagebox
import time


#Import the turtle module
import turtle
t = turtle.Turtle()
t.screen.setworldcoordinates(-300,-300,300,300)
#Max animation speed
t.speed(0)
#Change the background color of the screen
t.screen.bgcolor("black")
#Load the background image
t.screen.bgpic("starfield.gif")
#Hide the turtle
t.ht()
#Set the undo buffer to 1 (to save memory and speed things up)
t.setundobuffer(1)
#Speed up drawing (Draw every 2 frames)
t.screen.tracer(2)
#Register shapes
t.screen.register_shape("enemy.gif")
t.screen.register_shape("ally.gif")

class Sprite(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed = 0
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 0
		
	def is_collision(self, other):
		return (self.xcor() >= (other.xcor() - 20)) and \
			(self.xcor() <= (other.xcor() + 20)) and \
			(self.ycor() >= (other.ycor() - 20)) and \
			(self.ycor() <= (other.ycor() + 20))
			
	def move(self):
		self.fd(self.speed)

		if self.xcor() < -290:
			self.rt(60)
			self.setx(-290)
		
		elif self.xcor() > 290:
			self.rt(60)
			self.setx(290)
			
		if self.ycor() < -290:
			self.rt(60)
			self.sety(-290)		
		
		elif self.ycor() > 290:
			self.rt(60)
			self.sety(290)
		# part C
		if -250 < self.xcor() < -110 and 110 < self.ycor() < 190 or \
			-250 < self.xcor() < -180 and -170 < self.ycor() < 180 or \
			-250 < self.xcor() < -100 and -180 < self.ycor() < -120:
			self.lt(60)
		# Past S
		if -75 < self.xcor() < 70 and 120 < self.ycor() <180 or \
			-75 < self.xcor() < -10 and -70 < self.ycor() < 180 or \
			-75 < self.xcor() < 70 and -40 < self.ycor() < 20 or \
			-15 < self.xcor() < 70 and -180 < self.ycor() < 20 or \
			-75 < self.xcor() < 70 and -180 < self.ycor() < -125:
			self.lt(60)
		# Part 2
		if 120 < self.xcor() < 240 and 85 < self.ycor() < 180 or \
			180 < self.xcor() < 240 and -50 < self.ycor() < 180 or\
			120 < self.xcor() < 240 and -50 < self.ycor() < 5 or\
			120 < self.xcor() < 175 and -180 < self.ycor() < 15 or\
			120 < self.xcor() < 240 and -180 < self.ycor() < -120:
			self.lt(60)

class Player(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 0
		self.lives = 3
		self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
	
	def move(self):
		self.fd(self.speed)
		
		if self.xcor() < -290:
			self.setx(290)
		
		elif self.xcor() > 290:
			self.setx(-290)
			
		if self.ycor() < -290:
			self.sety(290)		
		
		elif self.ycor() > 290:
			self.sety(-290)	
	
	def turn_left(self):
		self.lt(25)
		
	def turn_right(self):
		self.rt(25)
				
	def accelerate(self):
		self.speed += 1
		
class Enemy(Sprite):
	def __init__(self, spriteshape,color,startx, starty):
		Sprite.__init__(self, spriteshape, color, startx,starty)
		self.speed = 5
		self.setheading(random.randint(0,360))
		if self.xcor() < -290:
			self.rt(60)
			self.setx(-290)
		
		elif self.xcor() > 290:
			self.rt(60)
			self.setx(290)
			
		if self.ycor() < -290:
			self.rt(60)
			self.sety(-290)		
		
		elif self.ycor() > 290:
			self.rt(60)
			self.sety(290)

class Ally(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid=0.7,stretch_len=0.7,outline=0)
		self.speed = 2
		self.setheading(random.randint(0,360))
			
	def avoid(self, other):
		if (self.xcor() >= (other.xcor() -20)) and \
			(self.xcor() <= (other.xcor() + 20)) and \
			(self.ycor() >= (other.ycor() -20)) and \
			(self.ycor() <= (other.ycor() + 20)):	
			self.lt(30)

class Bullet(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
		self.status = "ready"
		self.speed = 30
		
	def fire(self):
		if self.status == "ready":
			self.status = "shoot"
		
	def move(self):
		if self.status == "ready":
			self.hideturtle()
			#Move the turtle offscreen
			self.goto(-1000,1000)
		
		if self.status == "shoot":
			winsound.PlaySound("Laser_Blasts.wav",winsound.SND_ASYNC)
			self.goto(player.xcor(), player.ycor())
			self.setheading(player.heading())
			self.showturtle()
			self.status = "firing"
		
		if self.status == "firing":
			self.fd(self.speed)
			# part C
			if -235 < self.xcor() < -130 and 130 < self.ycor() < 170 or \
			-235 < self.xcor() < -195 and -170 < self.ycor() < 170 or \
			-235 < self.xcor() < -130 and -170 <self.ycor() < -130:
				self.goto(-1000,1000)
			# Past S
			if -60 < self.xcor() < 40 and 128 <self.ycor() <170 or \
			-60 < self.xcor() < -25 and -40 < self.ycor() < 170 or \
			-60 < self.xcor() < 40 and -40 <self.ycor() < 5 or \
			0 < self.xcor() < 40 and -170 <self.ycor() < 5 or \
			-60 < self.xcor() < 40 and -170 < self.ycor() < -131:
				self.goto(-1000,1000)
			# Part 2
			if 128< self.xcor() < 234 and 95 < self.ycor() < 170 or \
			195 < self.xcor() < 234 and -37 <self.ycor() < 170 or\
			125 < self.xcor() < 235 and -40 <self.ycor() < 7 or\
			125 < self.xcor() < 168 and -170 < self.ycor() < 7 or\
			128 < self.xcor() < 234 and -170 < self.ycor() < -130:
				self.goto(-1000,1000)
				
			#Border Check	
			if self.xcor() < -290 or self.xcor() > 290 \
				or self.ycor() < -290 or self.ycor() > 290:
				self.status = "ready"			
			
class Particle(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, -1000, -1000)
		self.frame = 0
		self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
		
	def explode(self, startx, starty):
		t.screen.tracer(4)
		self.goto(startx, starty)
		self.setheading(random.randint(0, 360))
		self.frame = 1

		
	def move(self):
		if self.frame != 0:
			self.fd(18-self.frame)
			self.frame += 1
			
			if self.frame < 6:
				self.shapesize(stretch_wid=0.3, stretch_len=0.3, outline=None)
			elif self.frame < 11:
				self.shapesize(stretch_wid=0.2, stretch_len=0.2, outline=None)
			else:
				self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
			
			if self.frame > 18:
				self.frame = 0
				self.goto(-1000, -1000)
				t.screen.tracer(2)
						
class Game():
	def __init__(self):
		self.score = 0
		self.state = "splash"
		self.pen = turtle.Turtle()
		self.lives = 3
		self.high_score = 0

	def draw_border(self):
		#Draw Border
		self.pen.speed(0)
		self.pen.color("white")
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.goto(-300, 300)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.penup()
	
	def draw_walls(self):
		# Letter C
		self.pen.speed(0)
		self.pen.color("white","white")
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.begin_fill()
		self.pen.goto(-233, 166)
		self.pen.pendown()
		self.pen.fd(100)
		self.pen.rt(90)
		self.pen.fd(33)
		self.pen.rt(90)
		self.pen.fd(66)
		self.pen.lt(90)
		self.pen.fd(266)
		self.pen.lt(90)
		self.pen.fd(66)
		self.pen.rt(90)
		self.pen.fd(33)
		self.pen.rt(90)
		self.pen.fd(100)
		self.pen.rt(90)
		self.pen.fd(332)
		self.pen.rt(90)
		self.pen.end_fill()
		self.pen.penup
		#Letter S
		self.pen.penup()
		self.pen.begin_fill()
		self.pen.goto(-50,166)
		self.pen.pendown()
		self.pen.fd(100)
		self.pen.rt(90)
		self.pen.fd(33)
		self.pen.rt(90)
		self.pen.fd(66)
		self.pen.lt(90)
		self.pen.fd(133)
		self.pen.lt(90)
		self.pen.fd(66)
		self.pen.rt(90)
		self.pen.fd(166)
		self.pen.rt(90)
		self.pen.fd(100)
		self.pen.rt(90)
		self.pen.fd(33)
		self.pen.rt(90)
		self.pen.fd(66)
		self.pen.lt(90)
		self.pen.fd(100)
		self.pen.lt(90)
		self.pen.fd(66)
		self.pen.rt(90)
		self.pen.fd(199)
		self.pen.rt(90)
		self.pen.end_fill()
		#number 2
		self.pen.penup()
		self.pen.begin_fill()
		self.pen.goto(132,166)
		self.pen.pendown()
		self.pen.fd(100)
		self.pen.rt(90)
		self.pen.fd(199)
		self.pen.rt(90)
		self.pen.fd(66)
		self.pen.lt(90)
		self.pen.fd(100)
		self.pen.lt(90)
		self.pen.fd(66)
		self.pen.rt(90)
		self.pen.fd(33)
		self.pen.rt(90)
		self.pen.fd(100)
		self.pen.rt(90)
		self.pen.fd(166)
		self.pen.rt(90)
		self.pen.fd(66)
		self.pen.lt(90)
		self.pen.fd(133)
		self.pen.lt(90)
		self.pen.fd(33)
		self.pen.lt(90)
		self.pen.fd(33)
		self.pen.rt(90)
		self.pen.fd(33)
		self.pen.rt(90)
		self.pen.fd(66)
		self.pen.rt(90)
		self.pen.end_fill()

		self.pen.penup()

	def show_status(self):
		self.pen.undo()
		if game.lives > 0:
			msg = "Lives: %s Score: %s High Score: %s " %(self.lives, self.score, self.high_score)		
		else: 
			msg = "Game Over Score: %s" %(self.score)
		self.pen.penup()
		self.pen.goto(-300, 310)
		self.pen.write(msg, font=("Arial", 16, "normal"))

#Create game object
game = Game()

#Draw the game border
game.draw_border()
game.draw_walls()

#Show the score
game.show_status()

#Create player and enemy objects
player = Player("triangle", "white", 80, 0.0)
#enemy = Enemy("circle", "red", 100.0, 0.0)
bullet = Bullet("triangle", "yellow", 0.0, 0.0)
#ally = Ally("square", "blue", 100, 100)

#Keyboard Bindings
t.screen.onkey(player.turn_left, "Left")
t.screen.onkey(player.turn_right, "Right")
t.screen.onkey(player.accelerate, "Up")
t.screen.onkey(bullet.fire, "space")
t.screen.listen()

#Set up the game
#Create lists for sprites
#Add Enemies

if game.state == "splash":
	enemies = []

	for e in range(4):
		if e%2 == 0:
			x = random.randint(-200, 200)
			y = random.randint(180, 290)
			enemies.append(Enemy("enemy.gif","red", x, y))
		else:
			x = random.randint(-200, 200)
			y = random.randint(-290, -180)
			enemies.append(Enemy("enemy.gif","red", x, y))

	#Add Allies
	allies = []
	for a in range(4):
		if a%2 == 0:
			x = random.randint(-200, 200)
			y = random.randint(180, 290)
			allies.append(Ally("ally.gif", "blue", x, y))
		else:
			x = random.randint(-200, 200)
			y = random.randint(-290, -180)
			allies.append(Ally("ally.gif", "blue", x, y))
		
	particles = []

	for p in range(2):
		particles.append(Particle("circle", "yellow", -1000, -1000))
	for p in range(2):
		particles.append(Particle("circle", "red", -1000, -1000))
	for p in range(2):
		particles.append(Particle("circle", "orange", -1000, -1000))

	game.state = "playing"

while True:
	time.sleep(0.02)
	if game.state == "restart":
		game.lives = 3
		game.score = 0
		player.speed = 0
		player.goto(70,0)
		player.setheading(0)
		game.show_status()

		i = 0
		for enemy in enemies:
			if i == 0:
				enemy.speed = 5
				enemy.goto(random.randint(-200, 200), random.randint(-290, -180))
				i += 1
			elif i == 1 :
				enemy.speed = 5
				enemy.goto(random.randint(-200, 200), random.randint(180, 290))
				i += 1
			elif i == 2:
				enemy.speed = 5
				enemy.goto(random.randint(-110, -90), random.randint(-120, 120))
				i += 1
			elif i == 3:
				enemy.speed = 5
				enemy.goto(random.randint(90, 110), random.randint(-120, 120))
				i += 1

		j = 0	
		for ally in allies:
			if j == 0:
				ally.speed = 2 
				ally.goto(random.randint(-200, 200), random.randint(-290, -180))
				j += 1
			elif j == 1:
				ally.speed = 2
				ally.goto(random.randint(-200, 200), random.randint(180, 290))
				j += 1
			elif j == 2:
				ally.speed = 2
				ally.goto(random.randint(-110, -90), random.randint(-120, 120))
				j += 1
			elif j == 3:
				ally.speed = 2
				ally.goto(random.randint(90, 110), random.randint(-120, 120))
				j += 1

		game.state = "playing"
	
	if game.state == "playing":
		player.move()
		bullet.move()
	
		for enemy in enemies:	
			enemy.move()

			#Check collisions
			if player.is_collision(enemy):
				winsound.PlaySound("crash.wav",winsound.SND_ASYNC)
				player.color("red")
				for particle in particles:
					particle.explode(enemy.xcor(), enemy.ycor())
				player.rt(random.randint(100, 200))
				enemy.goto(random.randint(-200, 200), random.randint(180, 290))
				ran = random.randint(0,1)
				if ran == 1:
					enemy.goto(random.randint(-200, 200), random.randint(180, 290))	
				else:
					enemy.goto(random.randint(-200, 200), random.randint(-290, -180))
				enemy.speed += 1
				game.lives -= 1
				if game.lives < 1:
					game.state = "gameover"
				game.show_status()
				player.color("white")
		
			if bullet.is_collision(enemy):
				winsound.PlaySound("collision.wav",winsound.SND_ASYNC) 
				for particle in particles:
					particle.explode(enemy.xcor(), enemy.ycor())
					
				bullet.status = "ready"
				enemy.goto(random.randint(-200, 200), random.randint(180, 290))
				ran = random.randint(0,3)
				if ran == 0:
					enemy.goto(random.randint(-200, 200), random.randint(180, 290))	
				elif ran == 1:
					enemy.goto(random.randint(-200, 200), random.randint(-290, -180))
				elif ran == 2:
					enemy.goto(random.randint(-110, -90), random.randint(-120, 120))
				else:
					enemy.goto(random.randint(60, 110), random.randint(-120, 120)) 
				enemy.speed += 1
				game.score += 100
				game.show_status()
			
		for ally in allies:
			ally.move()
			
			#Avoid enemy
			for enemy in enemies:	
				ally.avoid(enemy)

			#Allies should avoid player as well	
			ally.avoid(player)
	
			#Check collisions
			if bullet.is_collision(ally):
				winsound.PlaySound("collision.wav",winsound.SND_ASYNC)
				for particle in particles:
					particle.explode(ally.xcor(), ally.ycor())
				bullet.status = "ready"
				ran = random.randint(0,1)
				if ran == 0:
					ally.goto(random.randint(-200, 200), random.randint(180, 290))	
				elif ran == 1:
					ally.goto(random.randint(-200, 200), random.randint(-290, -180))
				elif ran == 2:
					ally.goto(random.randint(-110, -90), random.randint(-120, 120))
				else:
					ally.goto(random.randint(60, 110), random.randint(-120, 120))

				ally.speed += 1
				game.score -= 50
				game.show_status()
		# part C
		if -240 < player.xcor() < -125 and 120 < player.ycor() < 175 or \
			-240 < player.xcor() < -185 and -170 < player.ycor() < 170 or \
			-240 < player.xcor() < -125 and -170 < player.ycor() < -125:
			winsound.PlaySound("crash.wav",winsound.SND_ASYNC)
			player.color("red")
			for particle in particles:
				particle.explode(player.xcor(), player.ycor())
			player.bk(15)
			player.speed = 0
			ran = random.randint(0,1)
			game.lives -= 1
			if game.lives < 1:
				game.state = "gameover"
			game.show_status()
			player.color("white")
		# Past S
		elif -60 < player.xcor() < 40 and 128 < player.ycor() <170 or \
			-60 < player.xcor() < -25 and -40 < player.ycor() < 170 or \
			-60 < player.xcor() < 40 and -40 < player.ycor() < 5 or \
			0 < player.xcor() < 40 and -170 < player.ycor() < 5 or \
			-60 < player.xcor() < 40 and -170 < player.ycor() < -131:
			winsound.PlaySound("crash.wav",winsound.SND_ASYNC)
			player.color("red")
			for particle in particles:
				particle.explode(player.xcor(), player.ycor())
			player.bk(15)
			player.speed = 0
			ran = random.randint(0,1)
			game.lives -= 1
			if game.lives < 1:
				game.state = "gameover"
			game.show_status()
			player.color("white")
		# Part 2
		elif 128< player.xcor() < 234 and 95 < player.ycor() < 170 or \
			195 < player.xcor() < 234 and -37 < player.ycor() < 170 or\
			128 < player.xcor() < 234 and -37 < player.ycor() < 4 or\
			128 < player.xcor() < 167 and -170 < player.ycor() < 4 or\
			128 < player.xcor() < 234 and -170 < player.ycor() < -130:
			winsound.PlaySound("crash.wav",winsound.SND_ASYNC)
			player.color("red")
			for particle in particles:
				particle.explode(player.xcor(), player.ycor())
			player.bk(15)
			player.speed = 0
			ran = random.randint(0,1)
			game.lives -= 1
			if game.lives < 1:
				game.state = "gameover"
			game.show_status()
			player.color("white")

	for particle in particles:
		particle.move()
				
	if game.state == "gameover":
		winsound.PlaySound("game_over.wav",winsound.SND_ASYNC)
		if game.score > game.high_score:
			game.high_score = game.score
		for i in range(360):
			player.rt(1)
		
		if messagebox.askyesno("Game Over", "Play again?") == True:
			game.state = "restart"
		else:
			exit()
			turtle.done()