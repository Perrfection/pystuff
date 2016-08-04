import
 pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (700,500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Wolf Ravish")

Done = False

clock = pygame.time.Clock()


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
			
			
		#-----game logic
			
			
			
		#-----screen- clearing 
		screen.fill(WHITE)
		
		
		#-----drawing code
		pygame.draw.rect(rect(screen, RED, Rect, width=20) -> Rect)
		rect(Surface, color, Rect, width=0) -> Rect.draw.rect(screen, RED, (0,0, 700, 500))
		
		
		#----update screen with drawing
		pygame.display.flip()
		#pygame.display.update
		
		
		#-----limit to 60 frames per sec
		clock.tick(60)
		
pygame.quit()
exit()
		
		