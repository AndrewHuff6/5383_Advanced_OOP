# Pygame client - Week 3 (draws the game state that the server sends)
import asyncio
import json
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
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Andrew's Football Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
small_font = pygame.font.Font(None, 24)

# field layout: a 100 yard field with a 10 yard end zone on each side (120 yards total)
field_left = 50
field_top = 115
field_height = 330
yard_px = 7.5
end_zone_px = int(10 * yard_px)
FIELD_width = int(120 * yard_px)

# colors
white = (255, 255, 255)
grass = (34, 139, 34)
backdrop = (20, 70, 20)
home_color = (30, 60, 140)   # left end zone
away_color = (140, 30, 30)   # right end zone
ball_color = (139, 69, 19)
first_down_color = (255, 215, 0)

# filled in if the JavaScript bridge fails to start, so the error shows on screen
startup_error = ""


# browsers deliver WebSocket events through callbacks, so a small piece of JavaScript
# opens the connection and stores the connection status and the newest message from the
# server on the window object. the game loop below just reads those two values each frame.
def start_websocket(url):
    window.eval(f"""
        window.fb_status = 'connecting';
        window.fb_state = '';
        window.fb_ws = new WebSocket('{url}');
        window.fb_ws.onopen = function() {{ window.fb_status = 'connected'; }};
        window.fb_ws.onmessage = function(event) {{ window.fb_state = event.data; }};
        window.fb_ws.onerror = function() {{ window.fb_status = 'error'; }};
        window.fb_ws.onclose = function() {{ window.fb_status = 'closed'; }};
    """)


# returns the connection status and the newest message (a JSON string) from the server
def read_websocket():
    if not IN_BROWSER:
        return "not in browser (run with pygbag)", ""
    if startup_error:
        return "bridge error", ""
    try:
        return str(window.fb_status), str(window.fb_state)
    except Exception as e:
        return "read error", ""


# converts a distance from the LEFT goal line (0 to 100 yards) into an x pixel position
def yard_to_x(yard):
    return field_left + end_zone_px + int(yard * yard_px)


# the server sends field_position as yards from the possessing team's OWN end zone.
# the home team moves left to right, so the away team's position is measured from the right.
def ball_yard(state):
    if state["possession"] == "home":
        return state["field_position"]
    return 100 - state["field_position"]


# draws text with its top-left corner at (x, y)
def draw_text(text, x, y, fnt=None):
    surface = (fnt or font).render(text, True, white)
    screen.blit(surface, (x, y))


# draws the empty field: end zones, grass, yard lines, and yard numbers
def draw_field():
    screen.fill(backdrop)

    # end zones and playing field
    pygame.draw.rect(screen, home_color, (field_left, field_top, end_zone_px, field_height))
    pygame.draw.rect(screen, away_color, (field_left + FIELD_width - end_zone_px, field_top,
                                          end_zone_px, field_height))
    pygame.draw.rect(screen, grass, (yard_to_x(0), field_top, int(100 * yard_px), field_height))

    # a line every 5 yards, thicker every 10
    for yard in range(0, 101, 5):
        thickness = 3 if yard % 10 == 0 else 1
        x = yard_to_x(yard)
        pygame.draw.line(screen, white, (x, field_top), (x, field_top + field_height), thickness)

    # yard numbers (10, 20, 30, 40, 50, 40, 30, 20, 10)
    for yard in range(10, 100, 10):
        label = small_font.render(str(min(yard, 100 - yard)), True, white)
        screen.blit(label, label.get_rect(center=(yard_to_x(yard), field_top + field_height - 20)))

    # outline around the whole field
    pygame.draw.rect(screen, white, (field_left, field_top, FIELD_width, field_height), 3)


# draws the ball marker, the first down line, and the text using the data from the server
def draw_state(state):
    yard = ball_yard(state)
    mid_y = field_top + field_height // 2

    # yellow first down line: the home team drives right, the away team drives left
    direction = 1 if state["possession"] == "home" else -1
    first_down_yard = max(0, min(100, yard + direction * state["yards_to_go"]))
    x_first = yard_to_x(first_down_yard)
    pygame.draw.line(screen, first_down_color, (x_first, field_top), (x_first, field_top + field_height), 3)

    # the ball
    ball_x = yard_to_x(yard)
    pygame.draw.ellipse(screen, ball_color, (ball_x - 13, mid_y - 8, 26, 16))
    pygame.draw.ellipse(screen, white, (ball_x - 13, mid_y - 8, 26, 16), 2)

    # text readout of what the server sent
    name = state["teams"][state["possession"]]
    draw_text(f"{name} has the ball  |  Down {state['down']} & {state['yards_to_go']}"
              f"  |  Quarter {state['quarter']}", 50, 42)
    draw_text(f"{state['teams']['home']} {state['score']['home']}  -  "
              f"{state['score']['away']} {state['teams']['away']}", 50, 72)


# draws one full frame
def draw_screen(status, state):
    draw_field()
    draw_text(f"Connection: {status}", 50, 12)
    if state is None:
        draw_text("Waiting for game data from the server...", 330, field_top + field_height // 2 - 10)
    else:
        draw_state(state)
    pygame.display.flip()


async def main():
    global startup_error

    # open the connection once, before the loop starts
    if IN_BROWSER:
        try:
            start_websocket(SERVER_URL)
        except Exception as e:
            startup_error = str(e)

    state = None        # the newest game state received from the server
    last_text = ""      # the last message we parsed, so we only parse new ones

    # set to true by default
    running = True
    while running:
        for event in pygame.event.get():
            # if quit, quit the game
            if event.type == pygame.QUIT:
                running = False

        status, text = read_websocket()

        # a new message arrived from the server: turn the JSON text into a dictionary
        if text and text != last_text:
            last_text = text
            try:
                message = json.loads(text)
                if message.get("type") == "state":
                    state = message
            except ValueError:
                pass

        draw_screen(status, state)

        clock.tick(60)
        await asyncio.sleep(0)  # required for the browser build
    # quit the game if no longer running
    pygame.quit()


# run main
asyncio.run(main())