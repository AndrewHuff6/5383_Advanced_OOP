# Pygame window skeleton - Week 2 (browser-compatible via Pygbag, now with a WebSocket)
import asyncio
import sys
import pygame

# the browser build is the only place a WebSocket is available
IN_BROWSER = sys.platform == "emscripten"
if IN_BROWSER:
    import platform  # in pygbag, platform.window is the browser's JavaScript "window"
    window = platform.window

# address of the server (use ws://localhost:8765 when testing on your own computer)
SERVER_URL = "ws://localhost:8765"

# initialize the game
pygame.init()

# establish window dimensions
WIDTH = 1000
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Andrew's Football Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

# filled in if the JavaScript bridge fails to start, so the error shows on screen
startup_error = ""


# browsers deliver WebSocket events through callbacks, so a small piece of JavaScript
# opens the connection and stores the latest status and reply on the window object.
# the game loop below just reads those two values each frame.
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


# returns the connection status and the latest reply from the server
def read_websocket():
    if not IN_BROWSER:
        return "not in browser (run with pygbag)", ""
    if startup_error:
        return "bridge error", startup_error
    try:
        return str(window.fb_status), str(window.fb_reply)
    except Exception as e:
        return "read error", str(e)


# draws one line of white text on the field
def draw_text(text, y):
    surface = font.render(text, True, (255, 255, 255))
    screen.blit(surface, (40, y))


async def main():
    global startup_error

    # open the connection once, before the loop starts
    if IN_BROWSER:
        try:
            start_websocket(SERVER_URL)
        except Exception as e:
            startup_error = str(e)

    # set to true by default
    running = True
    while running:
        for event in pygame.event.get():
            # if quit, quit the game
            if event.type == pygame.QUIT:
                running = False

        status, reply = read_websocket()

        screen.fill((34, 139, 34))  # make the field green
        draw_text("Week 2 client", 20)  # if you can't see this, the browser is running old code
        draw_text(f"Connection: {status}", 80)
        draw_text("Sent: hello", 140)
        draw_text(f"Server replied: {reply}", 200)
        pygame.display.flip()

        clock.tick(60)
        await asyncio.sleep(0)  # required for the browser build
    # quit the game if no longer running
    pygame.quit()


# run main
asyncio.run(main())