import sys
from dataclasses import dataclass

"""
Want to parse the string: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
New line is a seperator of games.
- Replace Game with G, red with R, blue with B, green with G as this makes parsing easier.
- Split on :
- then split on ;
- then split on ,

"""
@dataclass
class Game:
    game_id : int
    max_blue: int
    max_green: int
    max_red: int

def _replace_text( text:str) -> str:
    text = text.replace( "Game", "G" )
    text = text.replace( "blue", "b" )
    text = text.replace( "green", "g" )
    text = text.replace( "red", "r" )
    text = text.replace( " ", "" )
    return text

def _read_input(filename: str) -> list[str]:
    with open(filename) as f:
        lines = _replace_text(f.read())
    return lines.splitlines()

def _parse_data(data:list[str]) -> list[Game]:
    games: list[Games] = []
    for game in data:
        game = game.split(':')
        # Get the game id
        game_id = int(game[0][1:])
        max_blue = 0
        max_green = 0
        max_red = 0

        moves = game[1].split(';')
        for move in moves:
            plays = move.split(',')
            for play in plays:
                color = play[-1]
                if color == 'g':
                    green = int(play[0:-1])
                    max_green = green if green > max_green else max_green
                if color == 'r':
                    red = int(play[0:-1])
                    max_red = red if red > max_red else max_red
                if color == 'b':
                    blue = int(play[0:-1])
                    max_blue = blue if blue > max_blue else max_blue
        games.append( Game( game_id=game_id, max_blue=max_blue, max_green=max_green, max_red=max_red ) )
    return games

def _get_valid_games( games:list[Game], max_red: int, max_blue: int, max_green: int) -> list[Game]:
    return [ g for g in games if g.max_red <= max_red and g.max_blue <= max_blue and g.max_green <= max_green ]



if __name__ == "__main__":
    file = sys.argv[1]
    data = _read_input(file)
    games = _parse_data(data)
    print(games)
    valid_games = _get_valid_games( games, 12,14,13 )
    total = sum( [ g.game_id for g in valid_games ] )
    print(total)
    part_2_total = sum( [g.max_blue * g.max_red * g.max_green for g in games ] )
    print( part_2_total)
