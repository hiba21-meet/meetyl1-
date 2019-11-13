from turtle import Turtle
class Ball(Turtle):
	def __init__(self,radius,color,dx,dy):
		Turtle.__init__(self)
		self.radius =radius
		self.dx=dx
		self.dy=dy
		self.penup()
		self.shape("circle")
		self.color(color)
	def move(self,screen_width,screen_height): 
		curent_x=xpos()
		new_x = current_x + self.dx
		right_side_ball = new_x + radius
		left_side_ball = new_x + radius
		bottom_side_ball = new_x + radius
		top_side_ball = new_x + radius
		ball.goto(50,50)
		screen_width=turtle.getcanvas().winfo_width()/2
		screen_height=turtle.getcanvas().winfo_height()/2

ball1=Ball(5,"red",12,3)
while 2==2:
	ball1.goto(2,2)
	ball1.goto(424,428)
ball1.move(10,20)
ball1.move(30,40)


		


		
		
		

