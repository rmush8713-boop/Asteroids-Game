import pygame
import sys
from constants import *
from logger import log_state
from logger import log_event
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    
    score = 0
    font = pygame.font.Font("calibri.ttf", 32)
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    AsteroidField()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}.\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:

        text = font.render(f"Score: {score}", 1, "white")
        screen.fill("black")
        screen.blit(text, (0, 0))

        dt = clock.tick(60) / 1000
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score += 1

            if player.collides_with(asteroid):
                log_event("player_hit")
                print(f"Game over!\nYou get {score} score!")
                sys.exit()

        pygame.display.flip()
        clock.tick(60)
        

if __name__ == "__main__":
    main()
