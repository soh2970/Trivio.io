import pygame 
import sys 


# initializing the constructor 
pygame.init() 

# screen resolution 
res = (844,600) 

# opens up a window 
screen = pygame.display.set_mode(res) 

# grey for esc button
color_esc = (220,220,220) 

# black color of text
color = (0,0,0) 
base_font= pygame.font.Font(None, 32)
user_text=' '
pass_text=' '

# light blue shade of the button 
color_button = (159,197,248) 

#rectangle
username_rect= pygame.Rect(400, 250, 200, 32)
password_rect= pygame.Rect(400, 300, 200, 32)


# stores the width of the 
# screen into a variable 
width = screen.get_width() 

# stores the height of the 
# screen into a variable 
height = screen.get_height() 

# defining a font 
mode_font= pygame.font.SysFont('Corbel',16) 
smallerfont = pygame.font.SysFont('Corbel',32) 
smallfont = pygame.font.SysFont('Corbel',60) 
bigfont= pygame.font.SysFont('Corbel',72) 

# rendering a text written in 
# this font 
username=smallfont.render('Username:' , True , color)
password=smallfont.render('Password:' , True , color)
login = bigfont.render('Log in to' , True , color) 
started = bigfont.render('get STARTED' , True , color) 
esc = smallfont.render('x' , True , color) 
ok = smallerfont.render('OK' , True , color) 
debug_mode = mode_font.render('Debugger mode' , True , color) 
instruct_mode = mode_font.render('Instructor mode' , True , color) 

pass_text=''
user_text=''

#exit click
while True: 
    for ev in pygame.event.get(): 
        
        if ev.type == pygame.QUIT: 
            pygame.quit() 
            
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
            
            #if the mouse is clicked on the 
            # x button the game is terminated 
            if width/2-405 <= mouse[0] <= width/2-385 and height/2-293 <= mouse[1] <= height/2-263: 
                pygame.quit() 
            if width/2+100 <= mouse[0] <= width/2+145 and height/2+50 <= mouse[1] <= height/2+80: 
                print (user_text)
                print (pass_text)
                sys.exit() 
            


            
            
        if ev.type == pygame.KEYDOWN:
            #username
            if width/2-22 <= mouse[0] <= width/2+178 and height/2-50 <= mouse[1] <= height/2-18:
                    #check for backspace
                    if ev.key == pygame.K_BACKSPACE:
                        #get text input
                        user_text = user_text[:-1]
                    else:
                        user_text += ev.unicode
            #password
            if width/2-22 <= mouse[0] <= width/2+178 and height/2 <= mouse[1] <= height/2+32:
                    if ev.key == pygame.K_BACKSPACE:
                        #get text input
                        pass_text = pass_text[:-1]
                    else:
                        pass_text += ev.unicode
            
        
    
        
    # fills the screen with a color: white 
    screen.fill((255,255,255)) 
    
    #draw rectangle for usernamse input
    pygame.draw.rect(screen, color_esc, username_rect)
    username_surface = base_font.render(user_text, True, (0, 0, 0))
    screen.blit(username_surface, (username_rect.x+5, username_rect.y+5))
    
    #draw rectangle for usernamse input
    pygame.draw.rect(screen, color_esc, password_rect)
    password_surface = base_font.render(pass_text, True, (0, 0, 0))
    screen.blit(password_surface, (password_rect.x+5, password_rect.y+5))
    

    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
    
    #button
    pygame.draw.rect(screen,color_button,[width/2+100,height/2+50,45,30]) 
    pygame.draw.rect(screen,color_esc,[width/2-405,height/2-293,30,30]) 
    pygame.draw.rect(screen,color_esc,[width/2-350,height/2-290,90,20]) 
    pygame.draw.rect(screen,color_esc,[width/2-350,height/2-265,90,20]) 


    # superimposing the text onto our button 
    screen.blit(login, (width/2-200,height/2-200))
    screen.blit(started, (width/2-50,height/2-150))
    screen.blit(esc , (width/2-400,height/2-300)) 
    screen.blit(username, (150, 245))
    screen.blit(password, (165, 290))
    screen.blit(ok, (width/2+105, height/2+55))
    screen.blit(debug_mode, (width/2-349, height/2-285))
    screen.blit(instruct_mode, (width/2-348, height/2-260))





    
    # updates the frames of the game 
    pygame.display.update() 
