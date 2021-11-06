from turtle import *

lives = 3
score = 0
lvl = 1

WIDTH, HEIGHT = 300, 300


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.setworldcoordinates(-150, -150, 150, 150)


#objects vars
objectImages = {
	"bg":"/Users/hugomasson/Desktop/Code/Python/FroggerGameClone/assets/bgImg.gif",
	"frog":"/Users/hugomasson/Desktop/Code/Python/FroggerGameClone/assets/frog.gif",
	"obstacles":"/Users/hugomasson/Desktop/Code/Python/FroggerGameClone/assets/obstacle.gif"
}

obstacles = {	#[x, y, dep, drawObject]
	1:[-150,120,"right",""],
	2:[-150,90,"left",""],
	3:[-150,60,"right",""],
	4:[-150,30,"left",""],
	5:[-150,0,"right",""],
	6:[-150,-30,"left",""],
	7:[-150,-60,"right",""],
	8:[-150,-90,"left",""],
}
player = {		#[x*30, y*30, lifesLeft, drawObject]
	0:[0,0,0,""]	
}
objective = {
	0:[0, 150, ""]
}
textDisplayed = {
	"lives":"",
	"score":"",
	"lvl":"",
	"gameOver":""
}

screen.addshape(objectImages["frog"])
screen.addshape(objectImages["obstacles"])


#drawing

def drawObject(path, x, y, speed):
	turtle1 = Turtle()
	turtle1.speed(speed)
	turtle1.shape(path)
	turtle1.penup()
	turtle1.goto(x, y)
	return turtle1

#player functions

def initPlayer():
	player[0][0] = 0
	player[0][1] = -120
	player[0][2] = 3
	player[0][3] = drawObject(objectImages["frog"], player[0][0], player[0][1], 0)

def isLost():
	for i in range(1, len(obstacles)+1):
		if player[0][1] == obstacles[i][1]:
			if abs(player[0][0]-obstacles[i][0])<=30:

				return True
	return False

def isWin():
	if player[0][0] == objective[0][0] and player[0][1] == 150:

		return True
	return False

def playerUp():
	if player[0][1]+30 <= 150:
		player[0][1] += 30
		player[0][3].goto(player[0][0], player[0][1])
def playerDown():
	if player[0][1]-30 >= -150:
		player[0][1] -= 30
		player[0][3].goto(player[0][0], player[0][1])
def playerRight():
	if player[0][0]+30 <= 150:
		player[0][0] += 30
		player[0][3].goto(player[0][0], player[0][1])
def playerLeft():
	if player[0][0]-30 >= -150:
		player[0][0] -= 30
		player[0][3].goto(player[0][0], player[0][1])


#obstacles functions

def initObstacles():
	for i in range(1,len(obstacles)+1):
		obstacles[i][3] = drawObject(objectImages["obstacles"], obstacles[i][0], obstacles[i][1], 0)
		

def nextGameTick():		#called every game tick
	pass

#objective functions

def initObjective():
	player[0][2] = drawObject(objectImages["frog"], objective[0][0], objective[0][1], 0)


def write(x, y, txt, s=15, c="white"):
	style = ('Courier', s)
	t = Turtle()
	t.color(c)
	t.penup()
	t.goto(x, y)
	t.write(txt,font=style)
	t.hideturtle()
	return t

a = write(-150,-10, "INSTRUCTIONS   HELP FROGGY REACH HOME\n  PRESS UP TO START", 10, "black")

def fun(speed=200):

	if isLost():
		player[0][0] = 0
		player[0][0] = -120

		clearAll()
		initAll()
		global lives
		lives -= 1
		textDisplayed["lives"].clear()
		textDisplayed["lives"] = write(50,130, "lives: "+str(lives))
		return
	elif isWin():
		player[0][0] = 0
		player[0][0] = -120

		clearAll()
		initAll()
		global score
		score += 100
		global lvl
		lvl+=1
		textDisplayed["score"].clear()
		textDisplayed["score"] = write(50,110, "score: "+str(score))
		textDisplayed["lvl"].clear()
		textDisplayed["lvl"] = write(50,90, "lvl: "+str(lvl))
		return
	for i in range(1, len(obstacles)+1):
		if obstacles[i][0] < -150:
			obstacles[i][0] = 150
		elif obstacles[i][0] > 150:
			obstacles[i][0] = -150
		else:
			pas = (10 if obstacles[i][2]=="left" else -10)
			obstacles[i][0] += pas
			obstacles[i][3].goto(obstacles[i][0], obstacles[i][1])
	if lives > 0:
		screen.ontimer(fun2, t=speed)

def initAll():


	#screen.bgpic(objectImages["bg"])
	initObjective()
	initObstacles()
	initPlayer()

def clearAll():
	player[0][3].hideturtle()
	for i in range(1, len(obstacles)+1):
		obstacles[i][3].hideturtle()

def fun2():

	if lives > 0:
		screen.ontimer(fun, t=200)

def gameOn():
	global a
	a.clear()
	#main frame (game)
	screen.bgpic(objectImages["bg"])
	initAll()

	textDisplayed["lives"] = write(50,130, "lives: "+str(player[0][2]))
	textDisplayed["score"] = write(50,110, "score: "+str(score))
	textDisplayed["lvl"] = write(50,90, "lvl: "+str(lvl))


	
	screen.onkey(playerUp, "Up")
	screen.onkey(playerDown, "Down")
	screen.onkey(playerLeft, "Left")
	screen.onkey(playerRight, "Right")

	global lives
	i = 0
	while lives > 0:		#in case we want to add lives the while is easier than for
		fun(200+i*20)		#time between every step => 50,40... ms
		i+=1
	

	style = ('Courier', 30)
	t = Turtle()
	t.color('white')
	t.penup()
	t.goto(-50, 50)
	t.write("GAME OVER",font=style)
	t.hideturtle()

def main():
	

	screen.listen()
	
	screen.onkey(gameOn, "Up")

	screen.mainloop()



main()





