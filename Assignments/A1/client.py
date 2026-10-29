import asyncio
import sys

# This file only works in the browser build (pygbag). Plain "python main.py" has no
# browser WebSocket to use, so stop early with a clear message.
if sys.platform != "emscripten":
    print("Run this with:  pygbag football_web   (then open the page from the Ports tab)")
    sys.exit()

import platform  # in pygbag, platform.window is the browser's JavaScript "window"
import pygame

window = platform.window

# Copy this from the Ports tab (port 8765 > Forwarded Address) and change https:// to wss://
SERVER_URL = "wss://solid-train-6prjpwqwvgvf5q6r-8765.app.github.dev"

pygame.init()
WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Andrew's Football Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)


# Browsers deliver WebSocket events through callbacks, so a small piece of JavaScript
# opens the connection and stores the latest status and reply on the window object.
# The game loop below just reads those two values each frame.
def start_websocket(url):
    window.eval(f"""
        window.fb_status = 'connecting';
        window.fb_reply = '';
        window.fb_ws = new WebSocket('{url}');
        window.fb_ws.onopen = function() {{
            window.fb_status = 'connected';
            window.fb_ws.send('hello');
        }};
        window.fb_ws.onmessage = function(event) {{
            window.fb_reply = event.data;
        }};
        window.fb_ws.onerror = function() {{ window.fb_status = 'error'; }};
        window.fb_ws.onclose = function() {{ window.fb_status = 'closed'; }};
    """)


def read_websocket():
    return str(window.fb_status), str(window.fb_reply)


def draw_text(text, y):
    surface = font.render(text, True, (255, 255, 255))
    screen.blit(surface, (40, y))


async def main():
    start_websocket(SERVER_URL)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        status, reply = read_websocket()

        screen.fill((34, 139, 34))  # field green
        draw_text(f"Connection: {status}", 40)
        draw_text("Sent: hello", 100)
        draw_text(f"Server replied: {reply}", 160)
        pygame.display.flip()

        clock.tick(60)
        await asyncio.sleep(0)  # required so the browser stays responsive

    pygame.quit()


asyncio.run(main())