import pygame

pygame.init()
window= pygame.display.set_mode(size=(600,480))
print('setup end')

print('loop start ')

while True :
    # CHECK FOR ALL EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # close window
            quit() #end pygame