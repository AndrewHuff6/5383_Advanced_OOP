# Week 2 - Minimal WebSocket server
# Accepts a client, prints whatever it sends, and replies to it.
# Later weeks will import Team / GameState from this same folder.

import asyncio
import websockets
import json

from players import QuarterBack, RunningBack, WideReceiver, Deflineman, LineBacker, CornerBack
from team_info import Team
from game_info import GameState

PORT = 8765

# Week 3 - WebSocket server that owns the game
# Builds both teams from the existing classes, then sends the game state to the client as JSON.
# players.py, team_info.py and game_info.py are imported exactly as they are.

import asyncio
import json
import websockets

from players import QuarterBack, RunningBack, WideReceiver, Deflineman, LineBacker, CornerBack
from team_info import Team
from game_info import GameState

PORT = 8765

# builds the same two teams that driver.py builds
def build_game():
    # home team
    home_team = Team("Home Team",
                     [QuarterBack("Andrew"), RunningBack("John"), WideReceiver("Mike")],
                     [Deflineman("James"), LineBacker("David"), CornerBack("Chris")])

    # away team
    away_team = Team("Away Team",
                     [QuarterBack("Tom"), RunningBack("Jerry"), WideReceiver("Sam")],
                     [Deflineman("Bob"), LineBacker("Steve"), CornerBack("Alex")])
    # return the both teams along with the game state object
    return home_team, away_team, GameState(home_team, away_team)


home_team, away_team, game = build_game()

# To test that the ball marker follows the server's data, uncomment one line, then restart server.py:
# game.field_position = 60          # ball moves to the 60 yard line
# game.possession = away_team       # away team has the ball, so the marker flips to the right side


# packs the current game state into a dictionary that can be sent as JSON
def snapshot():
    return {
        "type": "state",
        "down": game.down,
        "yards_to_go": game.yards_to_go,
        "field_position": game.field_position,  # yards from the possessing team's own end zone
        "possession": "home" if game.possession is home_team else "away",
        "quarter": game.quarter,
        "score": {"home": home_team.score, "away": away_team.score},
        "teams": {"home": home_team.name, "away": away_team.name},
    }

# Runs once per connected client (one coroutine per connection)
async def handler(websocket):
    print("Client connected")
    try:
        await websocket.send(json.dumps(snapshot()))  # send the initial game state to the client
        print("Sent state:", snapshot())
        # Loops once for each message the client sends
        async for message in websocket:
            print(f"Received: {message}")
            try:
                data = json.loads(message)
            except ValueError:
                continue
            if data.get("type") == "get_state":
                await websocket.send(json.dumps(snapshot()))
    except websockets.ConnectionClosed:
        pass
    print("Client disconnected")


async def main():
    # 0.0.0.0 so other devices (or a Codespace's port forwarding) can reach the server
    async with websockets.serve(handler, "0.0.0.0", PORT):
        print(f"WebSocket server listening on port {PORT}")
        await asyncio.Future()  # run forever


asyncio.run(main())