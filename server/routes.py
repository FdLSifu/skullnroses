from server import app
from server.games import Game

# ToDo manage several games
game = Game(4)

@app.route('/')
@app.route('/index')
def index():

    text =  "############## Welcome To SkullnRoses #################\n"
    text += " Game online : 1\n"
    text += " ---------------\n"
    text += " State: "+game.status+" \n"
    text += " Players "+" ".join(game.list_player()) + " \n"


    
    game.add_player("bob")
    game.add_player("james")
    game.add_player("cool")
    game.add_player("brian")
    return text
    #return "Let's play to SkullnRoses!"
