import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)



pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE







# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	



    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(GREEN)
	x = random.randint(-10,10) #change stuff to mach screen size
	y = random.randint(-10,10)
	xp = 350 - x
	yp = 250 - y
    # --- Drawing code should go here
	circle = pygame.draw.circle(screen, BLUE, (xp, yp), 20)
	
	if xp == 20: #unnessisary 
		x * -1
	elif xp == 680:
		x * -1
	else:
		x = x
		
	if yp == 20:
		y * -1
	elif xp == 680:
		y * -1
	else:
		y = y
	

		#Make your circle move by changing its x coordinate and y coordinate. 
		#Make sure the circle bounces off walls instead of running into them.
		#Make your circle move in a random direction each time you load the game with a speed between -10 and 10. 
		#You’ll need to get a random number between -10 and 10. 
		#Make your circle a random size between 20px and 80px each time you load the game.
		#Add some colors to the pre-generated list.
		#Look up which numbers Python uses to create colors.
		#Have your program choose a random color from the list you created for the circle to be each time the game loads. 
		#Make your circle flash random colors from your list as it moves.


    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    #---Limit to 60 frames per second
	clock.tick(60)

#Close the window and quit.
pygame.quit()
exit() #Needed when using IDLE