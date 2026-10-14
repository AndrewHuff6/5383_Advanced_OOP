# Pygame window skeleton - Week 1 (browser-compatible via Pygbag)
import asyncio
import pygame

# initialize the game
pygame.init()

# establish window dimensions
WIDTH = 1000
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Andrew's Football Game")
clock = pygame.time.Clock()

async def main():
    # set to true by default
    running = True
    while running:
        for event in pygame.event.get():
            # if quit, quit the game
            if event.type == pygame.QUIT:
                running = False

        screen.fill((34, 139, 34))  # make the field green
        pygame.display.flip()

        clock.tick(60)
        await asyncio.sleep(0)  # required for the browser build
    # quit the game if no longer running
    pygame.quit()
# run main
asyncio.run(main())