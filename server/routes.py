import os
from flask import render_template,redirect,url_for
from flask import request
from flask import make_response
from server import app
from server.games import Game

app.config["EXPLAIN_TEMPLATE_LOADING"] = True
app.config["DEBUG"] = True

# ToDo manage several games
game = Game(4)

global text
def settext():
    global text
    text = []
    text.append("Game online : 1")
    text.append("State: "+game.status)
    text.append("Note: " +game.msg)
    text.append("Player:")
    text += game.players

def getcookie(req):
    if 'session_snr' in req:
        cookie = req['session_snr']
        game_id = cookie.split("_")[0]
        username = cookie.split("_")[1]
        return game_id,username
    return "",""


@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    settext()
    if 'session_snr' in request.cookies:
        game_id,username = getcookie(request.cookies)
        if game_id == game.id :
            username = cookie.split("_")[1]
            text.append("You are "+username)

    return render_template('index.html', text=text)

@app.route('/addplayer',methods=['GET','POST'])
def addplayer():
    # Get name from request
    name = request.form['playername']
    # Call add player
    game.add_player(request.form['playername'])
    settext()
    # Attribute a cookie
    resp = make_response(render_template('index.html',text=text))
    resp.set_cookie('session_snr',str(game.id)+str('_')+str(name))

    return resp

@app.route('/reset',methods=['GET','POST'])
def reset():
    global game
    game = Game(4)
    return index()

@app.route('/start',methods=['GET','POST'])
def start():
    game.launch()
    return refresh()

def refresh():
    game_id, username = getcookie(request.cookies)
    info = ""
    if game_id == game.id :
        player_id = game.get_playerid(username)
        play = False
        if game.turn == player_id:
            play = True
            info = "You have %s Roses and %s Skulls " % (game.players[player_id].getroses(),game.players[player_id].getskulls())
        return render_template('start.html',players=game.players,play=play,game=game,text=info)
    else:
        return index()
    
@app.route('/playskull',methods=['GET','POST'])
def playskull():
    game_id,username = getcookie(request.cookies)
    if game_id == game.id:
        player_id = game.get_playerid(username)
        if game.turn == player_id:
            p = game.players[player_id]
            if p.getskulls() > 0:
                game.turn = (game.turn + 1) % len(game.players)
                p.playskull()
    return redirect(url_for('start'))

@app.route('/playrose',methods=['GET','POST'])
def playrose():
    game_id, username = getcookie(request.cookies)
    if game_id == game.id:
        player_id = game.get_playerid(username)
        if game.turn == player_id:
            p = game.players[player_id]
            if p.getroses() > 0:
                game.turn = (game.turn + 1) % len(game.players)
                p.playrose()
    return redirect(url_for('start'))

