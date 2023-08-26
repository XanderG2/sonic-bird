import pygame, random, sys;pygame.init();pygame.font.init();myfont = pygame.font.SysFont("monospace", 15);white = (255,255,255);black = (0,0,0);grey = (128,128,128);yellow = (255,255,0);color = black;width = 1200;height = 800;screen = pygame.display.set_mode((width, height));pygame.display.set_caption("Flappy bird but very strange and also not really flappy bird its more like sonic because you have to collect the rings... ill call it sonic bird | Xander");highscore = 0
def main(): 
    global highscore;player = pygame.Rect(width//2,height//2,50,50);player.x -= player.width//2;player.y -= player.height//2;ring = pygame.Rect(width//2, height//2, 5, 75);clock = pygame.time.Clock();fps = 60;time_flashing = 0;lives = 3;score = -1;gravity = 0;direction = "r";running = True
    while running:
        clock.tick(fps);time_flashing -= 1
        if time_flashing >= 0 and time_flashing % 10 == 0 and color == grey: color = black
        elif time_flashing >= 0 and time_flashing % 10 == 0 and color == black: color = grey
        if time_flashing < 0:
            color = black
        if lives < 0: highscore = score if score > highscore else highscore;main()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False;sys.exit()
            if event.type == pygame.KEYDOWN: gravity = -5
        if direction == "r": player.x += 5
        else: player.x -= 5
        if player.x >= width - player.width: direction = "l"
        elif player.x <= 0: direction = "r"
        if player.y <= 0: gravity = 0; player.y = height//2;lives -= 1; time_flashing = 3*fps
        elif player.y >= height - player.height: gravity = 0; player.y = height//2;lives -= 1; time_flashing = 3*fps
        if player.colliderect(ring): ring.y = random.randint(0,height-ring.height);score += 1
        screen.fill(white);player.y += gravity;gravity += 0.1;pygame.draw.rect(screen, color, player);pygame.draw.rect(screen, yellow, ring);label = myfont.render(f"Lives: {lives}", 1, black);screen.blit(label, (width-label.get_width(), 0));label2 = myfont.render(f"Score: {score}", 1, black);screen.blit(label2, (0,0));label3 = myfont.render(f"High score: {highscore}", 1, black);screen.blit(label3, (width//2-label3.get_width()//2, 0));pygame.display.flip()
if __name__ == "__main__": main()