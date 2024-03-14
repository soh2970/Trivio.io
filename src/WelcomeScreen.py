import pygame 
import sys 


# initializing the constructor 
pygame.init() 

# screen resolution 
res = (844,600) 

# opens up a window 
screen = pygame.display.set_mode(res) 

# black color of text
color = (0,0,0) 

# light blue shade of the button 
color_light = (159,197,248) 

# stores the width of the 
# screen into a variable 
width = screen.get_width() 

# stores the height of the 
# screen into a variable 
height = screen.get_height() 

# defining a font 
smallfont = pygame.font.SysFont('Corbel',60) 
bigfont= pygame.font.SysFont('Corbel',72) 

# rendering a text written in 
# this font 
text = smallfont.render('START' , True , color) 
welcome = bigfont.render('WELCOME TO' , True , color) 
trivio = bigfont.render('T R I V I O' , True , color) 


while True: 
	
	for ev in pygame.event.get(): 
		
		if ev.type == pygame.QUIT: 
			pygame.quit() 
			
		#checks if a mouse is clicked 
		if ev.type == pygame.MOUSEBUTTONDOWN: 
			
			#if the mouse is clicked on the 
			# button the game is terminated 
			if width/2-100 <= mouse[0] <= width/2+100 and height/2+100 <= mouse[1] <= height/2+140: 
				pygame.quit() 
				
	# fills the screen with a color: white 
	screen.fill((255,255,255)) 
	
	# stores the (x,y) coordinates into 
	# the variable as a tuple 
	mouse = pygame.mouse.get_pos() 
	
    #button
	pygame.draw.rect(screen,color_light,[width/2-100,height/2+100,200,40]) 
	
	# superimposing the text onto our button 
	screen.blit(text , (width/2-65,height/2+100)) 
	screen.blit(welcome, (width/2-200,height/2-100))
	screen.blit(trivio, (width/2,height/2))

	
	# updates the frames of the game 
	pygame.display.update() 
